from django.urls import reverse
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "phone",
            "image",
            "bio"
        )

    def get_user(self, obj):
        user = {
            "user_id": obj.user.id,
            "username": obj.user.username,
            "email": obj.user.email,
            "full_name": obj.user.get_full_name,
            "url": reverse("user-detail", args=[obj.user.id])
        }
        return user
