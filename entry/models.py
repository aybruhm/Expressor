from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    name      = models.CharField(max_length=100)
    title     = models.CharField(max_length=200)
    content   = models.TextField(max_length=600, unique=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Entries'