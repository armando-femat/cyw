# Generated by Django 2.2.4 on 2019-08-31 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0002_auto_20190831_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='critere',
            old_name='Titre',
            new_name='titre',
        ),
        migrations.AlterField(
            model_name='liste',
            name='promesses',
            field=models.ManyToManyField(null=True, to='compare.Promesse'),
        ),
    ]
