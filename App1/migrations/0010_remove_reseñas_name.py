# Generated by Django 4.2.5 on 2023-10-05 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0009_cafeterias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reseñas',
            name='name',
        ),
    ]
