from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Post, Comment

User = get_user_model()


class PostAdminArea(admin.ModelAdmin):
    list_display = ("title", "author", "date_created")


admin.site.register(Post, PostAdminArea)
admin.site.register(Comment)
