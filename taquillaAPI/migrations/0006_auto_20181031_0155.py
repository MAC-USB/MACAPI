# Generated by Django 2.1 on 2018-10-31 01:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taquillaAPI', '0005_auto_20181031_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='preparador',
            name='correo',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Email invalido', regex='([a-zA-Z0-9_-]+\\.?){1,}@[a-z]+\\.[a-z]{1,}')]),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='tipo',
            field=models.CharField(max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Tipo invalido', regex='[a-zA-Z]+')]),
        ),
        migrations.AddField(
            model_name='venta',
            name='notas',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cedula',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Cedula invalida', regex='^[V|E|J|P]\\-[0-9]{5,8}$')]),
        ),
        migrations.AlterField(
            model_name='plataformapago',
            name='nombre',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='Nombre invalido', regex='[a-zA-Z]+')]),
        ),
        migrations.AlterField(
            model_name='preparador',
            name='cedula',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Cedula invalida', regex='^[V|E|J|P]\\-[0-9]{5,8}$')]),
        ),
    ]