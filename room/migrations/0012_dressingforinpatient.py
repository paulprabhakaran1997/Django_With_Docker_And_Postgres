# Generated by Django 4.1 on 2022-09-27 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patient_gender'),
        ('room', '0011_rename_investigations_dischargesummary_in_investigation'),
    ]

    operations = [
        migrations.CreateModel(
            name='DressingForINPatient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dressing', models.CharField(max_length=100, null=True)),
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
    ]
