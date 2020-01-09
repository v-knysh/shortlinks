import datetime

from django.db.models import Max, Count
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets

from api.models import Link, LinkAction
from api.serializers import LinkSerializer


def unwrap_shortlink(request, short_url):
    link = get_object_or_404(Link, short_url=short_url)
    location = link.redirect_location
    lo = LinkAction(
        link=link,
        target_ip_address=request.user_ip,
        action_datetime=datetime.datetime.now()
    )
    lo.save()
    return redirect(location)


def index(request):
    return HttpResponse("<h1>Hello!</h1>")


class LinksViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    
    def get_queryset(self):
        user_ip = self.request.user_ip
        return Link.objects.filter(author_ip=user_ip).annotate(count=Count("actions")).annotate(
            last_action=Max("actions__action_datetime"))
