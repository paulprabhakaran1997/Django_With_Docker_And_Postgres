# Generated by Django 4.1 on 2022-09-19 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='in_patient_paymenttransactions',
            name='assignroom',
        ),
        migrations.RemoveField(
            model_name='in_patient_paymenttransactions',
            name='ip_payment',
        ),
        migrations.RemoveField(
            model_name='in_patient_paymenttransactions',
            name='patient',
        ),
        migrations.DeleteModel(
            name='IN_Patient_Payments',
        ),
        migrations.DeleteModel(
            name='IN_Patient_PaymentTransactions',
        ),
    ]