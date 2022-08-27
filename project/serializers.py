from django.urls import reverse
from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    # owner = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)
    owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "code_link",
            "demo_link",
            "thumbnail",
            "owner",
            "date_created",
            "date_updated",
        )

    def get_owner(self, obj):
        owner = {
            "id": obj.owner.id,
            "username": obj.owner.username,
            "url": reverse("user-detail", args=[obj.owner.id])
        }
        return owner
