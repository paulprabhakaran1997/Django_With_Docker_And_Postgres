# Generated by Django 4.0.6 on 2023-02-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0046_alter_labtestforoutpatient_payment_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanforoutpatient',
            name='payment_complete',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
