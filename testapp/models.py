from django.db import models

# Create your models here.
class URL(models.Model):
    url = models.URLField()
    hidden_url = models.CharField(max_length=10)