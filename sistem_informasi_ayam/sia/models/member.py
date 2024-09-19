from django.db import models

class Members(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=13)

    def __str__(self):
        return self.name