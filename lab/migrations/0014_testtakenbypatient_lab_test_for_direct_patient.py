# Generated by Django 4.0.6 on 2022-11-04 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0013_labtestfordirectpatient_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtakenbypatient',
            name='lab_test_for_direct_patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lab.labtestfordirectpatient'),
        ),
    ]
