# Generated by Django 2.2.8 on 2020-01-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0034_auto_20200115_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='ville',
            name='url',
            field=models.CharField(default=models.CharField(max_length=100, unique=True), max_length=100, unique=True),
        ),
    ]
