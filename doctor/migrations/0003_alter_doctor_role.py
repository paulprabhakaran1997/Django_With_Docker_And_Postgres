# Generated by Django 4.0.3 on 2022-08-08 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
        ('doctor', '0002_alter_doctor_created_time_alter_doctor_updated_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hospital.role'),
        ),
    ]
