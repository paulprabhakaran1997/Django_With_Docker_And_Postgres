# Generated by Django 4.1 on 2022-09-26 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_doctor_role'),
        ('patient', '0002_patient_gender'),
        ('ward', '0007_rename_ip_payment_ward_patient_paymenttransactions_ward_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DischargeSummary_Ward',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_surgery', models.DateTimeField(null=True)),
                ('allergies', models.CharField(max_length=500, null=True)),
                ('diagnosis', models.CharField(max_length=500, null=True)),
                ('investigation', models.CharField(max_length=500, null=True)),
                ('treatment', models.CharField(max_length=500, null=True)),
                ('advice_on_discharge', models.CharField(max_length=500, null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('consultant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.doctor')),
                ('ip_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.assignward')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
                ('ward_bed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.wardbed')),
            ],
            options={
                'verbose_name_plural': 'DischargeSummary_Ward',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]
