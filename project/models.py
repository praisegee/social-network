from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    code_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
