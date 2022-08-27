from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.SET_NULL)
    members = models.ManyToManyField(to=User, related_name="members")
    image = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Communities"

    def __str__(self):
        return self.name

    @property
    def get_total_members(self):
        total_members = self.members.all()
        return len(total_members)
