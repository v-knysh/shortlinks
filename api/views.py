import datetime
import random

from django.db import IntegrityError
from django.db.models import Max, Count
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Link, LinkAction
from api.serializers import LinkSerializer, LinkAddSerializer


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


class LinksViewSet(viewsets.ViewSet):
    def list(self, request):
        users_links_queryset = self._base_queryset(request.user_ip)
        serializer = LinkSerializer(users_links_queryset, many=True, context={'request': request})
        return Response(serializer.data, )

    def retrieve(self, request, pk=None):
        queryset = self._base_queryset(request.user_ip)
        link_query = get_object_or_404(queryset, id=pk)
        serializer = LinkSerializer(link_query, context={'request': request})
        return Response(serializer.data)

    def _base_queryset(self, user_ip):
        return Link.objects.filter(author_ip=user_ip).annotate(count=Count("actions")).annotate(last_action=Max("actions__action_datetime"))

    def create(self, request):
        serializer = LinkAddSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        redirect_location = serializer.validated_data['redirect_location']
        for i in range(10):
            try:
                short_url = random_string()
                link = Link(
                    short_url=short_url,
                    created=datetime.datetime.now(),
                    author_ip=request.user_ip,
                    redirect_location=redirect_location,
                )
                link.save()
            except IntegrityError:
                pass
            else:
                break
        else:
            return Response("Something went wrong", status=500)
        return Response(LinkSerializer(link).data)


def random_string():
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    res = []
    for i in range(6):
        res.append(random.choice(s))
    return "".join(res)