# Generated by Django 4.0.6 on 2022-11-22 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ward', '0015_rename_others_ward_patient_payments_consultant_charges_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ward_patient_paymenttransactions',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
