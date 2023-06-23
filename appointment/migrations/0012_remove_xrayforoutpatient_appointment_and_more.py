# Generated by Django 4.0.5 on 2022-08-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0011_remove_appointment_lab_checked_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xrayforoutpatient',
            name='appointment',
        ),
        migrations.RemoveField(
            model_name='xrayforoutpatient',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='outpatient_payments',
            name='card',
        ),
        migrations.RemoveField(
            model_name='outpatient_payments',
            name='lab',
        ),
        migrations.RemoveField(
            model_name='outpatient_payments',
            name='xray',
        ),
        migrations.RemoveField(
            model_name='outpatient_paymenttransactions',
            name='card',
        ),
        migrations.AddField(
            model_name='appointment',
            name='lab_checked',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='lab_test',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='xray_checked',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='xray_test',
            field=models.JSONField(null=True),
        ),
        migrations.DeleteModel(
            name='LabTestForOutPatient',
        ),
        migrations.DeleteModel(
            name='XrayForOutPatient',
        ),
    ]
