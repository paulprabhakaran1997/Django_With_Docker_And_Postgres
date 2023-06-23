# Generated by Django 4.0.3 on 2022-11-29 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patient_pos_id'),
        ('appointment', '0029_outpatient_payments_payment_recived_by_xray'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='has_scan',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='outpatient_payments',
            name='payment_recived_by_scan',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='outpatient_payments',
            name='scan',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='ScanForOutPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('scan_test', models.JSONField(null=True)),
                ('scan_checked', models.BooleanField(default=False, null=True)),
                ('scan_test_date', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'ScanForOutPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]