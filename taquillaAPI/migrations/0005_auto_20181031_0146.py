# Generated by Django 2.1 on 2018-10-31 01:46

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taquillaAPI', '0004_auto_20181030_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagodeuda',
            name='fecha_pago',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='pagodeuda',
            name='tipoPago',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]