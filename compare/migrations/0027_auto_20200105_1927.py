# Generated by Django 2.2.8 on 2020-01-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0026_liste_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='liste',
            name='couleur',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidat',
            name='EstTeteDeListe',
            field=models.BooleanField(default=False),
        ),
    ]
