from django.contrib import admin
from .models import Project


class ProjectAdminView(admin.ModelAdmin):
    search_fields = ("title", "owner")
    list_display = ("title", "owner", "date_updated")


admin.site.register(Project, ProjectAdminView)
