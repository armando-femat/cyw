# Generated by Django 2.2.8 on 2020-01-14 22:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0032_auto_20200114_2341'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Candidat',
        ),
        migrations.AlterField(
            model_name='liste',
            name='auteur',
            field=models.ManyToManyField(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
