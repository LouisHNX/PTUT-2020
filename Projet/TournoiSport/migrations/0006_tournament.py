# Generated by Django 3.1.5 on 2021-01-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TournoiSport', '0005_team_idteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTournament', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
