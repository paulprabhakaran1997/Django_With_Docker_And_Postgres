# Generated by Django 4.0.6 on 2023-02-17 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0009_scanforpatient_op_scan_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanpaymenttransaction',
            name='scan_for_direct_patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='scan.scanfordirectpatient'),
        ),
    ]
