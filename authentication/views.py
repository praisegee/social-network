from django.contrib.auth import get_user_model, authenticate, login, logout

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    AuthUserSerializer
)

User = get_user_model()


class UserRegisterAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")

            user = authenticate(
                request=request,
                email=email,
                password=password
            )

            if not user:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_403_FORBIDDEN)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                data = {
                    "user_info": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email
                    },
                    "token": token.key
                }

                return Response(data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        Token.objects.get(user=user).delete()
        logout(request)
        return Response({"detail": "Log out"}, status=status.HTTP_200_OK)


class AuthUserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer


class AuthUserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer
    lookup_field = "pk"


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
