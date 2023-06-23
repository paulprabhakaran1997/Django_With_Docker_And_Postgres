# Generated by Django 4.1 on 2022-09-19 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0003_alter_doctor_role'),
        ('patient', '0002_patient_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignRooms',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('checkup', models.IntegerField(default=0, null=True)),
                ('has_room', models.BooleanField(default=False, null=True)),
                ('has_lab', models.BooleanField(default=False, null=True)),
                ('has_xray', models.BooleanField(default=False, null=True)),
                ('doctor_prescription', models.TextField(default='', null=True)),
                ('assigned_date', models.DateTimeField(null=True)),
                ('reason', models.TextField(default='', null=True)),
                ('discharged_date', models.DateTimeField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('initially_paid', models.BooleanField(default=False, null=True)),
                ('payment_pending', models.BooleanField(default=True, null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'AssignRooms',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='DocterCheckup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.assignrooms')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.doctor')),
            ],
            options={
                'verbose_name_plural': 'DocterCheckup',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='IN_Patient_Payments',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('doctor_fees', models.IntegerField(default=0, null=True)),
                ('injection', models.IntegerField(default=0, null=True)),
                ('service', models.IntegerField(default=0, null=True)),
                ('others', models.IntegerField(default=0, null=True)),
                ('lab', models.IntegerField(default=0, null=True)),
                ('xray', models.IntegerField(default=0, null=True)),
                ('total', models.IntegerField(default=0, null=True)),
                ('paid', models.IntegerField(default=0, null=True)),
                ('balance', models.IntegerField(default=0, null=True)),
                ('cash', models.IntegerField(default=0, null=True)),
                ('upi', models.IntegerField(default=0, null=True)),
                ('card', models.IntegerField(default=0, null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.assignrooms')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'IN_Patient_Payments',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_no', models.CharField(max_length=150, null=True)),
                ('room_type', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
                ('description', models.TextField(null=True)),
                ('vacancy_status', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Rooms',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='XrayForINPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('xray_test', models.JSONField(null=True)),
                ('xray_checked', models.BooleanField(default=False, null=True)),
                ('xray_test_date', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.assignrooms')),
                ('doctor_checkup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.doctercheckup')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'XrayForINPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MedicineForINPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('medicine_list', models.JSONField(null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.assignrooms')),
                ('doctor_checkup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.doctercheckup')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'MedicineForINPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='LabTestForINPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('lab_test', models.JSONField(null=True)),
                ('lab_checked', models.BooleanField(default=False, null=True)),
                ('lab_test_date', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.assignrooms')),
                ('doctor_checkup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.doctercheckup')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'LabTestForINPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='InjectionForINPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.assignrooms')),
                ('doctor_checkup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.doctercheckup')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'InjectionForINPatient',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='IN_Patient_PaymentTransactions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('total', models.IntegerField(default=0, null=True)),
                ('existing_balance', models.IntegerField(default=0, null=True)),
                ('paid', models.IntegerField(default=0, null=True)),
                ('balance', models.IntegerField(default=0, null=True)),
                ('cash', models.IntegerField(default=0, null=True)),
                ('upi', models.IntegerField(default=0, null=True)),
                ('card', models.IntegerField(default=0, null=True)),
                ('payment_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.assignrooms')),
                ('ip_payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.in_patient_payments')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'IN_Patient_PaymentTransactions',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='doctercheckup',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.rooms'),
        ),
        migrations.AddField(
            model_name='assignrooms',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.rooms'),
        ),
    ]
