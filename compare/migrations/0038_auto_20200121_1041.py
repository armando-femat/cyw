# Generated by Django 2.2.8 on 2020-01-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0037_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='resteInforme',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='source',
            field=models.CharField(choices=[('ACC', 'Formulaire contact'), ('VSL', 'Ville sans liste'), ('VAL', 'Ville avec listes')], default='ACC', max_length=3),
        ),
    ]
