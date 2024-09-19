from django.db import models
from .member import Members

class HewanTernak(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    description= models.CharField(max_length=13)
    kategori = models.CharField(max_length=13)
    status = models.CharField(max_length=255)
    tanggal_masuk = models.DateField(max_length=255)
    user_id = models.ForeignKey(Members ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name