from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model() #noi qui non usiamo custom ma è sempre buona pratica

__all__ = ["Movie",
           "StreamingChannel",
           ]

# Create your models here.
class StreamingChannel(models.Model): #messo sopra così posso usarlo nella foreign key
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
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
    streaming_channel = models.ForeignKey(
        StreamingChannel, #primo:metodo collegato
        on_delete=models.PROTECT, 
        #che succ se SChannel viene eliminato? impedisce eliminaz finche ci sono film associati
        #to=,
        null=True,
        blank=True,
    )

def __str__(self):
    return self.title