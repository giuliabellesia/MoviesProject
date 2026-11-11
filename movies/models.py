from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model() #noi qui non usiamo custom ma è sempre buona pratica

__all__ = ["Movie"]

# Create your models here.
class Movie(models.Model):
    owner=models.ForeignKey(
            USER,
            on_delete=models.PROTECT,
            default=None,
            null=True,
            )
    title = models.CharField(max_length=250)
    subtitle = models.CharField(
            max_length=250,
            null=True,
            blank=True
        )
    director = models.CharField(max_length=100)
    description = models.CharField("", max_length=1000)

def __str__(self):
    return self.title