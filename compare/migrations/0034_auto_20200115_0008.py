# Generated by Django 2.2.8 on 2020-01-14 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0033_auto_20200114_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liste',
            name='couleur',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='liste',
            name='nom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
