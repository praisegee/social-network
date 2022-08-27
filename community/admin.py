from django.contrib import admin

from .models import Community


class AdminCommunityArea(admin.ModelAdmin):
    search_fields = ("name", "creator")
    list_display = ("name", "creator", "date_created")


admin.site.register(Community, AdminCommunityArea)
