from django.urls import re_path, path

from . import views

urlpatterns = [
    re_path('(?P<short_url>[a-zA-Z0-9]{6})/', views.unwrap_shortlink, name='unwrap'),
    path('', views.index, name='index'),
]