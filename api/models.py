from datetime import datetime

from django.db import models


class Link(models.Model):
    short_url = models.CharField(max_length=6)
    redirect_location = models.CharField(max_length=256)
    expiration_date = models.DateTimeField(null=True)
    created = models.DateTimeField()
    author_ip = models.GenericIPAddressField()
    is_active = models.BooleanField(default=True)


class LinkAction(models.Model):
    target_ip_address = models.GenericIPAddressField()
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='actions')
    action_datetime = models.DateTimeField()
