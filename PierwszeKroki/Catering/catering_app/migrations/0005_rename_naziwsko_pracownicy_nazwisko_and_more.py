# Generated by Django 4.1.3 on 2023-01-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering_app', '0004_remove_faktura_dostawca_towaru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pracownicy',
            old_name='naziwsko',
            new_name='nazwisko',
        ),
        migrations.AlterField(
            model_name='pracownicy',
            name='pesel',
            field=models.CharField(max_length=45),
        ),
    ]
