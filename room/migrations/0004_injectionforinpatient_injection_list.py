# Generated by Django 4.1 on 2022-09-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_in_patient_payments_in_patient_paymenttransactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='injectionforinpatient',
            name='injection_list',
            field=models.JSONField(null=True),
        ),
    ]