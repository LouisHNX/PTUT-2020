# Generated by Django 3.1.5 on 2021-01-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TournoiSport', '0003_auto_20210109_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='idPoolT',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]