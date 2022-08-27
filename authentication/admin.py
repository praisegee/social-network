from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from authentication.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Create password",
                                min_length=6, max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password",
                                min_length=6, max_length=30, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2"
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match!")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])

        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "username",
        )


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    search_fields = ("username", "email")
    list_display = ("username", "email", "last_login", "date_joined")
    list_filter = ()
    filter_horizontal = ()
    filter_vertical = ()

    fieldsets = (
        (None, {
            "fields": (
                "email",
                "first_name",
                "last_name",
                "username",
            ),
        }),
        ("Permission", {
            "fields": (
                "is_active",
                "is_admin",
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "first_name",
                "last_name",
                "username",
                "password1",
                "password2"
            ),
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
