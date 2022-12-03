# Generated by Django 4.1.3 on 2022-12-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering_app', '0003_alter_pracownicy_pesel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faktura',
            name='dostawca_towaru',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='posilk_klienta',
        ),
        migrations.RemoveField(
            model_name='magazyn',
            name='dostawca_towaru',
        ),
        migrations.AlterField(
            model_name='pracownicy',
            name='pesel',
            field=models.DecimalField(decimal_places=0, max_digits=11),
        ),
        migrations.DeleteModel(
            name='dostawca',
        ),
    ]
