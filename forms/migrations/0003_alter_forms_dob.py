# Generated by Django 4.0.6 on 2022-12-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_alter_forms_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='dob',
            field=models.DateTimeField(null=True),
        ),
    ]
