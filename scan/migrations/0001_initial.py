# Generated by Django 4.0.3 on 2022-11-29 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0003_patient_pos_id'),
        ('room', '0023_assignrooms_has_scan_and_more'),
        ('appointment', '0030_appointment_has_scan_and_more'),
        ('ward', '0017_assignward_balance_assignward_paid_assignward_total_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, null=True)),
                ('amount', models.IntegerField(default=0, null=True)),
                ('description', models.TextField(default='', null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Scan',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ScanForPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('total_amount', models.IntegerField(default=0, null=True)),
                ('balance', models.IntegerField(default=0, null=True)),
                ('initially_paid', models.BooleanField(default=False, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('patient_type', models.CharField(max_length=100, null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
                ('assignroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.assignrooms')),
                ('assignward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.assignward')),
                ('ip_scan_test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.scanforinpatient')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'ScanForPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ScanTakenByPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('scan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='scan.scan')),
                ('scan_for_patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='scan.scanforpatient')),
            ],
            options={
                'verbose_name_plural': 'ScanTakenByPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]
