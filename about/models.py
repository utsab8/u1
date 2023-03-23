from django.db import models

# Create your models here.

class About(models.Model):
    header = models.CharField(max_length=200)