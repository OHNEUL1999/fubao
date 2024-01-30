# Generated by Django 5.0.1 on 2024-01-30 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fish', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('lattitude', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
                ('join_fish_location', models.ManyToManyField(to='fish.fish')),
            ],
        ),
    ]
