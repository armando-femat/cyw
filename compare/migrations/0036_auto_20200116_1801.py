# Generated by Django 2.1.7 on 2020-01-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0035_ville_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ville',
            name='nom',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='ville',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
