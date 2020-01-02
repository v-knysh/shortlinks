from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

from api.models import Link


def unwrap_shortlink(request, short_url):
    link = get_object_or_404(Link, short_url=short_url)
    location = link.redirect_location
    return redirect(location)

def index(request):
    return HttpResponse("<h1>Hello!</h1>")
