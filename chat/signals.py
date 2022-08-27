# from django.utils.text import slugify
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from datetime import datetime as dt
#
# from .models import Group
#
#
# def format_date():
#     date_time = dt.now().strftime("%D %H %M %S")
#     return date_time.replace("/", "-")
#
#
# @receiver(pre_save, sender=Group)
# def pre_save_group_slug(sender, instance, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.name + format_date() + "-slug")