from rest_framework import serializers
from .models import CustomUser, Audio


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'id', 'uuid', 'password')

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)


class AudioSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Audio
        fields = ('file', 'id')

    def create(self, validated_data):
        return Audio.objects.create(**validated_data)
