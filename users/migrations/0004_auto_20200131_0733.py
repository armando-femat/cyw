# Generated by Django 2.2.8 on 2020-01-31 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200119_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_list',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ville',
        ),
    ]
