# Generated by Django 4.0.5 on 2022-08-29 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patient_gender'),
        ('appointment', '0007_appointment_medicine_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutPatient_Payments',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('doctor_fees', models.IntegerField(default=0, null=True)),
                ('injection', models.IntegerField(default=0, null=True)),
                ('one_touch', models.IntegerField(default=0, null=True)),
                ('dressing', models.IntegerField(default=0, null=True)),
                ('ecg', models.IntegerField(default=0, null=True)),
                ('neb', models.IntegerField(default=0, null=True)),
                ('total', models.IntegerField(default=0, null=True)),
                ('paid', models.IntegerField(default=0, null=True)),
                ('balance', models.IntegerField(default=0, null=True)),
                ('cash', models.IntegerField(default=0, null=True)),
                ('upi', models.IntegerField(default=0, null=True)),
                ('payment_date', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(null=True)),
                ('updated_time', models.DateTimeField(null=True)),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'OutPatient_Payments',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='OutPatient_PaymentTransactions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('total', models.IntegerField(default=0, null=True)),
                ('existing_balance', models.IntegerField(default=0, null=True)),
                ('paid', models.IntegerField(default=0, null=True)),
                ('balance', models.IntegerField(default=0, null=True)),
                ('cash', models.IntegerField(default=0, null=True)),
                ('upi', models.IntegerField(default=0, null=True)),
                ('payment_date', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(null=True)),
                ('updated_time', models.DateTimeField(null=True)),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
                ('op_payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.outpatient_payments')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
            options={
                'verbose_name_plural': 'OutPatient_PaymentTransactions',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]
