from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    create_password = serializers.CharField(
        style={"input_type": "password"},
        label="Create password",
        min_length=6,
        max_length=30,
        write_only=True
    )
    confirm_password = serializers.CharField(
        style={"input_type": "password"},
        label="Confirm password",
        min_length=6,
        max_length=30,
        write_only=True
    )

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "create_password",
            "confirm_password",
        )
        extra_kwargs = {
            "id": {"read_only": True}
        }

    def save(self, **kwargs):
        user = User(
            first_name=self.validated_data.get("first_name"),
            last_name=self.validated_data.get("last_name"),
            username=self.validated_data.get("username"),
            email=self.validated_data.get("email"),
        )

        password1 = self.validated_data.get("create_password")
        password2 = self.validated_data.get("confirm_password")

        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError({"password": ["Password don't match!"]})

        user.set_password(password2)
        user.save()

        return user

    def create(self, validated_data):
        User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    profile = serializers.HyperlinkedRelatedField(view_name="profile-detail", read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "profile",
            "is_admin",
            "last_login",
            "date_joined"
        )
        extra_kwarg = {
            "password": {"write_only": True}
        }




