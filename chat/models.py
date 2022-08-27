# from django.db import models
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# class Group(models.Model):
#     name = models.CharField(max_length=20)
#     members = models.ManyToManyField(User, related_name="group_members", blank=True)
#     creator = models.ForeignKey(User, related_name="group_creator", on_delete=models.CASCADE, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField(unique=True, blank=True, max_length=500)
#     # image = models.ImageField(default=None, blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
#     content = models.TextField()
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.content[:50]
