# Generated by Django 4.0.6 on 2023-02-17 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0047_scanforoutpatient_payment_complete'),
        ('scan', '0008_scanfordirectpatient_payment_complete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanforpatient',
            name='op_scan_test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.scanforoutpatient'),
        ),
    ]