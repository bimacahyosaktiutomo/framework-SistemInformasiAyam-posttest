from django.db import models


class Users(models.Model):
    OVERSEER = 1
    MEMBER = 2
    ROLE_CHOICES = (
        (OVERSEER, 'Overseer'),
        (MEMBER, 'Member'),
    )

    username = models.CharField(max_length=150, unique=True)
    # Panjang standar untuk password hash di Django
    password = models.CharField(max_length=128)
    role = models.IntegerField(choices=ROLE_CHOICES)


    def __str__(self):
        return self.username