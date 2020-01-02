import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

from api.models import Link, LinkOpening


def unwrap_shortlink(request, short_url):
    link = get_object_or_404(Link, short_url=short_url)
    location = link.redirect_location
    lo = LinkOpening(
        link=link,
        opener_ip_address=request.META.get('REMOTE_ADDR'),
        open_datetime=datetime.datetime.now()
    )
    lo.save()
    return redirect(location)

def index(request):
    return HttpResponse("<h1>Hello!</h1>")
