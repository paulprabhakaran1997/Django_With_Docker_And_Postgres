# Generated by Django 4.0.6 on 2023-01-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patient_pos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
