# Generated by Django 4.0.6 on 2022-10-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0023_outpatient_payments_others'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='medical_prescription',
            field=models.TextField(default='', null=True),
        ),
    ]
