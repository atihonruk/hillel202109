# Generated by Django 3.2.9 on 2021-12-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='key',
            field=models.SlugField(unique=True),
        ),
    ]
