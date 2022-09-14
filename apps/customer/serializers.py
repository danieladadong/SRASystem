from rest_framework import serializers
from apps.customer.models import User, Profile


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = User


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Profile
