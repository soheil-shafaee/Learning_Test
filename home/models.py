from django.db import models


class Post(models.Model):
    STATUS_CHOICES = (
        ("pub", "published"),
        ("drf", "draft"),
    )
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    city = models.CharField(max_length=50)
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
