# Generated by Django 4.0.5 on 2022-08-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0005_rename_appointment_id_labtestforpatient_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestforpatient',
            name='total_amount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
