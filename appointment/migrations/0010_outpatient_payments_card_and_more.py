# Generated by Django 4.0.5 on 2022-08-30 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0009_remove_outpatient_payments_payment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='outpatient_payments',
            name='card',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='outpatient_paymenttransactions',
            name='card',
            field=models.IntegerField(default=0, null=True),
        ),
    ]