from django.db import models


class Link(models.Model):
    short_url = models.CharField(max_length=6)
    redirect_location = models.CharField(max_length=256)
    expiration_date = models.DateTimeField()
    author_ip = models.GenericIPAddressField()
    is_active = models.BooleanField()


class LinkOpening(models.Model):
    opener_ip_address = models.GenericIPAddressField()
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    open_datetime = models.DateTimeField()
