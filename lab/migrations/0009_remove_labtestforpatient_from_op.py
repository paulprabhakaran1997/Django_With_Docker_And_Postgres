# Generated by Django 4.1 on 2022-09-23 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_labtestforpatient_assignward_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labtestforpatient',
            name='from_op',
        ),
    ]
