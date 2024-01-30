# Generated by Django 5.0.1 on 2024-01-30 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kor', models.CharField(max_length=100)),
                ('name_eng', models.CharField(max_length=100)),
                ('fish_difficulty', models.IntegerField()),
                ('area_id', models.ManyToManyField(to='information.fishing_area')),
                ('bait_id', models.ManyToManyField(to='information.fishing_bait')),
                ('equipment_id', models.ManyToManyField(to='information.fishing_equipment')),
                ('method_id', models.ManyToManyField(to='information.fishing_method')),
                ('prohibit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='information.prohibit_fish')),
                ('release_standard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='information.release_fish')),
            ],
        ),
        migrations.CreateModel(
            name='user_fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_length', models.FloatField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('preference', models.BooleanField(default=0)),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fish.fish')),
            ],
        ),
    ]
