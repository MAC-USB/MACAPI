# Generated by Django 2.1 on 2019-01-21 17:52

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountHistory',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('ideal_amount_cash', models.FloatField(default=0)),
                ('ideal_amount_account', models.FloatField(default=0)),
                ('real_amount_cash', models.FloatField(default=0)),
                ('real_amount_account', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id_document', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Invalid id document', regex='^[V|E|J|P]\\-[0-9]{5,8}$')])),
                ('initials', models.CharField(default=None, max_length=3, validators=[django.core.validators.RegexValidator(message='Invalid initials', regex='[A-Z]{2,3}')])),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Invalid first name', regex='^[a-zA-Záéíóúñ]+$')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Invalid last name', regex='^[a-zA-Záéíóúñ ]+$')])),
                ('email', models.EmailField(blank=True, max_length=40, null=True, validators=[django.core.validators.RegexValidator(message='Invalid email', regex='([a-zA-Z0-9_-]+\\.?){1,}@[a-z]+\\.[a-z]{1,}')])),
                ('debt_amount', models.FloatField(default=0)),
                ('debt_date', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='Invalid name', regex='^[a-zA-Záéíóúñ ]+$')])),
                ('code', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999)])),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_document', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Invalid document id', regex='^[V|E|J|P]\\-[0-9]{5,8}$')])),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Invalid first name', regex='^[a-zA-Záéíóúñ]+$')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Invalid last name', regex='^[a-zA-Záéíóúñ]+$')])),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Invalid Phone', regex='[(]?\\d{3}[)]?\\s?-?\\s?\\d{3}\\s?-?\\s?\\d{4}')])),
            ],
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'pending'), (2, 'processing'), (3, 'approved')])),
                ('assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taquillaAPI.Assistant')),
            ],
        ),
        migrations.CreateModel(
            name='DebtPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taquillaAPI.Assistant')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(default=0)),
                ('range_days', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Invalid name', regex='^[a-zA-Záéíóúñ/ ]+$')])),
                ('product_price', models.FloatField(default=0)),
                ('product_quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PayMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='Invalid description', regex='^[a-zA-Záéíóúñ ]+$')])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Invalid name', regex='^[a-zA-Záéíóúñ/ ]+$')])),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('notes', models.CharField(blank=True, max_length=60)),
                ('assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taquillaAPI.Assistant')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taquillaAPI.Client')),
                ('item', models.ManyToManyField(to='taquillaAPI.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.FloatField()),
                ('reference_number', models.IntegerField(default=0)),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taquillaAPI.Bank')),
                ('debt_payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taquillaAPI.DebtPayment')),
                ('pay_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taquillaAPI.PayMethod')),
                ('sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taquillaAPI.Sale')),
            ],
        ),
        migrations.AddField(
            model_name='debt',
            name='debt_payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taquillaAPI.DebtPayment'),
        ),
        migrations.AddField(
            model_name='debt',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taquillaAPI.Item'),
        ),
    ]
