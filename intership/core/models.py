from django.db import models

# Create your models here.
class Doubt(models.Model):
    subject = models.CharField(max_length=100)
    desc = models.TextField()