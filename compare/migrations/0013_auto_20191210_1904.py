# Generated by Django 2.2.4 on 2019-12-10 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0012_auto_20191115_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ville',
            old_name='nom',
            new_name='name',
        ),
    ]