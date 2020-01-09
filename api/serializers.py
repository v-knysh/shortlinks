from datetime import datetime

from django.utils.crypto import get_random_string
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from api.models import Link


class LinkSerializer(ModelSerializer):
    last_action = serializers.DateTimeField(default=None, read_only=False)
    count = serializers.IntegerField(default=0, read_only=False)

    class Meta:
        model = Link
        fields = "__all__"
        read_only_fields = [
            "last_action",
            "count",
            "short_url",
            "expiration_date",
            "created",
            "author_ip",
            "is_active",
        ]

    def to_representation(self, instance):
        host = self.context['request'].get_host()
        instance.short_url = f"http://{host}/{instance.short_url}"
        return super().to_representation(instance)

    def create(self, validated_data):
        user_ip = self.context['request'].user_ip
        short_url = get_random_string(length=6)
        link = Link(
            short_url=short_url,
            created=datetime.now(),
            author_ip=user_ip,
            redirect_location=validated_data["redirect_location"],
        )
        link.save()
        return link
