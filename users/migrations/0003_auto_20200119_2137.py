# Generated by Django 2.2.8 on 2020-01-19 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0028_liste_site'),
        ('users', '0002_auto_20200119_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_list',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='ville',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='compare.Ville'),
        ),
    ]
