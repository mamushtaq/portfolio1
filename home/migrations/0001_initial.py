# Generated by Django 3.2.4 on 2021-09-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graphics',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('title', models.TextField(max_length=128)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images')),
                ('link', models.TextField(default=None, max_length=1229)),
                ('title', models.TextField(max_length=128)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Websites',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images')),
                ('link', models.TextField(default=None, max_length=1229)),
                ('title', models.TextField(max_length=128)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
