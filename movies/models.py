from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.


class YTSMovie(models.Model):
    yts_id = models.PositiveIntegerField(unique=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


