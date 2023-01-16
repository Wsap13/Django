# Generated by Django 4.1.3 on 2023-01-14 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catering_app', '0007_alter_pracownicy_stanowisko'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posilki',
            name='typ',
            field=models.CharField(choices=[('norm', 'normalny'), ('wega', 'wegański'), ('wege', 'wegetariański')], default='norm', max_length=5),
        ),
        migrations.AlterField(
            model_name='zamowienia',
            name='posilki',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catering_app.posilki'),
        ),
    ]