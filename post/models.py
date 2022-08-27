from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    likes = models.ManyToManyField(to=User, related_name="likes")
    comments = models.ManyToManyField(to=User, related_name="comments")
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def get_total_likes(self):
        total_likes = self.likes.all()
        return len(total_likes)

    @property
    def get_total_comments(self):
        total_comments = self.comments.all()
        return len(total_comments)


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    @property
    def get_total_likes(self):
        total_likes = self.likes.all()
        return len(total_likes)

