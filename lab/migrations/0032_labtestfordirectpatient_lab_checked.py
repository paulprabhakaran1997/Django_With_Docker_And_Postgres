# Generated by Django 4.0.6 on 2023-02-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0031_labtestfordirectpatient_lab_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestfordirectpatient',
            name='lab_checked',
            field=models.BooleanField(default=False, null=True),
        ),
    ]