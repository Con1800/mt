from rest_framework import serializers
from .models import Helloapp

class HelloappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helloapp
        fields = "__all__"