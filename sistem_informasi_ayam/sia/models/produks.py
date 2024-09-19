from django.db import models

class Produks(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=13)
    description= models.CharField(max_length=255)
    kategori = models.CharField(max_length=13)
    stok = models.IntegerField()

    def __str__(self):
        return self.name