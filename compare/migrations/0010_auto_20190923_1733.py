# Generated by Django 2.2.4 on 2019-09-23 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0009_auto_20190917_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='nom',
            new_name='titre',
        ),
    ]
