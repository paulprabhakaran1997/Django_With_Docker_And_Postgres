# Generated by Django 4.1 on 2022-09-23 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ward', '0003_doctercheckup_ward_xrayforwardpatient_and_more'),
        ('lab', '0007_labtestforpatient_assignroom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestforpatient',
            name='assignward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.assignward'),
        ),
        migrations.AddField(
            model_name='labtestforpatient',
            name='ward_lab_test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ward.labtestforwardpatient'),
        ),
    ]
