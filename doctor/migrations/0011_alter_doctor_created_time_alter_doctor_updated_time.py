# Generated by Django 4.0.6 on 2023-02-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_alter_doctor_health_checkup_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
