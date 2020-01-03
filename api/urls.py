from django.urls import re_path, path, include
from rest_framework import routers

from . import views
from .views import LinksViewSet

router = routers.DefaultRouter()
router.register(r'links', LinksViewSet, 'links')

urlpatterns = [
    re_path('(?P<short_url>[a-zA-Z0-9]{6})/', views.unwrap_shortlink, name='unwrap'),
    path('', views.index, name='index'),
    path('api/', include(router.urls), name='links'),
]