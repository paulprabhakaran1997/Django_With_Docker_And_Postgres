# Generated by Django 4.0.6 on 2023-02-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0032_labtestfordirectpatient_lab_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestfordirectpatient',
            name='lab_canceled',
            field=models.BooleanField(default=False, null=True),
        ),
    ]