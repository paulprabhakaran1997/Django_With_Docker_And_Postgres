# Generated by Django 4.0.3 on 2022-08-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_alter_appointment_checkup'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='initially_paid',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
