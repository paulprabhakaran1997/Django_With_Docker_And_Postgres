# Generated by Django 4.1 on 2022-09-23 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patient_gender'),
        ('doctor', '0003_alter_doctor_role'),
        ('ward', '0002_assignward'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocterCheckup_Ward',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.assignward')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.doctor')),
                ('ward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.wards')),
                ('ward_bed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.wardbed')),
            ],
            options={
                'verbose_name_plural': 'DocterCheckup_Ward',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='XrayForWardPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('xray_test', models.JSONField(null=True)),
                ('xray_checked', models.BooleanField(default=False, null=True)),
                ('xray_test_date', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.assignward')),
                ('doctor_checkup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.doctercheckup_ward')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'XrayForWardPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MedicineForWardPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('medicine_list', models.JSONField(null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.assignward')),
                ('doctor_checkup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.doctercheckup_ward')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'MedicineForWardPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='LabTestForWardPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('lab_test', models.JSONField(null=True)),
                ('lab_checked', models.BooleanField(default=False, null=True)),
                ('lab_test_date', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.assignward')),
                ('doctor_checkup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.doctercheckup_ward')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'LabTestForWardPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='InjectionForWardPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('injection_list', models.JSONField(null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.assignward')),
                ('doctor_checkup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.doctercheckup_ward')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'InjectionForWardPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]
