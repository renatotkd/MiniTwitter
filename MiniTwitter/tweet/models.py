from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Tweet(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='tweets'
    )
    content = models.TextField(
        max_length=280
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
    likes = models.BigIntegerField(
        default=0
    )

    def __str__(self):
        return self.content

