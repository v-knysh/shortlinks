from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from api.models import Link


class LinkSerializer(ModelSerializer):
    requires_context = True
    last_action = serializers.DateTimeField(default=None)
    count = serializers.IntegerField(default=0)

    class Meta:
        model = Link
        fields = "__all__"

    def to_representation(self, instance):
        host = self.context['request'].get_host()
        instance.short_url = f"http://{host}/{instance.short_url}"
        return super().to_representation(instance)

class LinkAddSerializer(Serializer):
    redirect_location = serializers.URLField(max_length=256, allow_blank=False)