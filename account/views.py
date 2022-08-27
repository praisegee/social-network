from rest_framework import generics

from .serializers import ProfileSerializer
from .models import Profile


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "pk"

