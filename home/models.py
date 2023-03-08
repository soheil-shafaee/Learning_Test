from django.db import models

STATUS_CHOICES = (
    ("pub", "published"),
    ("drf", "draft"))


class Post(models.Model):
    text = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = STATUS_CHOICES

