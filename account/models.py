from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    followers = models.ManyToManyField(to=User, related_name="followers")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    @property
    def email(self):
        return self.user.email

    @property
    def full_name(self):
        return self.user.get_full_name

    @property
    def get_total_followers(self):
        followers = self.followers.all()
        return len(followers)
