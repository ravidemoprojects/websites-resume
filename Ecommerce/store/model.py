from django.db import models

class Catogory(models.Model):
    name = models.CharField(max_length=100)