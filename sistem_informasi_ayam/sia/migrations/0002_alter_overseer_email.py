# Generated by Django 5.1 on 2024-10-01 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overseer',
            name='email',
            field=models.EmailField(max_length=20, unique=True),
        ),
    ]
