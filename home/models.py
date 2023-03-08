from django.db import models

STATUS_CHOICES = (
    ("pub", "published"),
    ("drf", "draft"),
)


class Post(models.Model):
    title=models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title

