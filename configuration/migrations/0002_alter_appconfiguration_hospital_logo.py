# Generated by Django 4.1 on 2022-11-03 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appconfiguration',
            name='hospital_logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
