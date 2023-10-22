# Generated by Django 4.2.5 on 2023-10-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('opinion', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Velero',
            new_name='Suscriptos',
        ),
        migrations.DeleteModel(
            name='Albums',
        ),
        migrations.DeleteModel(
            name='Band_members',
        ),
    ]