# Generated by Django 4.0.6 on 2022-12-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0030_transferroom_created_time_transferroom_updated_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignrooms',
            name='balance_from_op',
            field=models.IntegerField(default=0, null=True),
        ),
    ]