from django.db import models
from django.utils import timezone

# Create your models here.
class Entry(models.Model):
    title    = models.CharField(max_length=200)
    content  = models.TextField(max_length=512, unique=True)
    timestap = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title