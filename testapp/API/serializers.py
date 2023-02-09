from testapp.models import URL
from rest_framework import serializers

class URLSerializer(serializers.Serializer):
    url = serializers.URLField()