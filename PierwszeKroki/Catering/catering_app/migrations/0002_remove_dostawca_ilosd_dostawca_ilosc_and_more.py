# Generated by Django 4.1.3 on 2022-11-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dostawca',
            name='ilosd',
        ),
        migrations.AddField(
            model_name='dostawca',
            name='ilosc',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='dostawca',
            name='nazwa_dostawcy',
            field=models.CharField(default='dostawca', max_length=90),
        ),
        migrations.AddField(
            model_name='posilki',
            name='typ',
            field=models.CharField(default='normalny', max_length=50),
        ),
        migrations.AddField(
            model_name='pracownicy',
            name='pesel',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dostawca',
            name='cena',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='faktura',
            name='rozliczenia',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='faktura',
            name='suma',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='klient',
            name='do_zaplaty',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='pracownicy',
            name='pensja',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]