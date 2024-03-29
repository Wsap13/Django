# Generated by Django 4.1.3 on 2022-11-19 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dostawca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('towary', models.CharField(max_length=45)),
                ('ilosd', models.IntegerField()),
                ('cena', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='posilki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posilek_nazwa', models.CharField(max_length=50)),
                ('cena', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='pracownicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('naziwsko', models.CharField(max_length=45)),
                ('stanowisko', models.CharField(max_length=45)),
                ('pensja', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='magazyn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('towary', models.CharField(max_length=45)),
                ('ilosc', models.IntegerField()),
                ('data_przydatnosci', models.DateTimeField()),
                ('dostawca_towaru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catering_app.dostawca')),
            ],
        ),
        migrations.CreateModel(
            name='klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zamowienie', models.CharField(max_length=50)),
                ('do_zaplaty', models.FloatField()),
                ('adres_klienta', models.CharField(max_length=50)),
                ('posilk_klienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catering_app.posilki')),
            ],
        ),
        migrations.CreateModel(
            name='faktura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suma', models.FloatField()),
                ('rozliczenia', models.FloatField()),
                ('data', models.DateField()),
                ('dostawca_towaru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catering_app.dostawca')),
                ('klient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catering_app.klient')),
            ],
        ),
    ]
