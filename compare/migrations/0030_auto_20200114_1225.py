# Generated by Django 2.2.8 on 2020-01-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0029_auto_20200111_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ville',
            old_name='ProfessionMaire',
            new_name='professionMaire',
        ),
        migrations.AddField(
            model_name='ville',
            name='ouverte',
            field=models.BooleanField(default=False),
        ),
    ]
