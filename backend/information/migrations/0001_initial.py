# Generated by Django 5.0.1 on 2024-01-30 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fishing_area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('document', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='fishing_bait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('document', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='fishing_equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('document', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='fishing_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('document', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='prohibit_fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kor', models.CharField(max_length=40)),
                ('name_eng', models.CharField(blank=True, max_length=50, null=True)),
                ('standard_start', models.DateField(null=True)),
                ('standard_end', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='release_fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kor', models.CharField(max_length=40)),
                ('name_eng', models.CharField(blank=True, max_length=50, null=True)),
                ('standard', models.FloatField(null=True)),
            ],
        ),
    ]
