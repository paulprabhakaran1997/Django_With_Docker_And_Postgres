# Generated by Django 4.0.6 on 2022-11-10 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0019_in_patient_payments_total_lab_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='in_patient_payments',
            name='total_lab_amount',
        ),
    ]