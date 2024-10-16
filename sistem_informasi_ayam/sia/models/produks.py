from uuid import uuid4
from django.db import models
import os

class Produks(models.Model):
    # id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    description= models.CharField(max_length=255)
    kategori = models.CharField(max_length=13)
    stok = models.IntegerField()
    image = models.ImageField(upload_to='produks/')

    def __str__(self):
        return self.name