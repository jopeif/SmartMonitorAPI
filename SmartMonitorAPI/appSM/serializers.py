
from rest_framework import serializers

class MySerializer(serializers.Serializer):
    field1 = serializers.CharField(max_length=100)