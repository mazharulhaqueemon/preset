from rest_framework import serializers

from .models import post,Catagores


class CatagoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagores
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = "__all__"


class CatagoiresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagores
        fields = "__all__"