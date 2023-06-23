# Generated by Django 4.0.6 on 2023-02-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0047_scanforoutpatient_payment_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctorcheckupamount',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctorcheckupamount',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='injectionforoutpatient',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='injectionforoutpatient',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='labtestforoutpatient',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='labtestforoutpatient',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicineforoutpatient',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicineforoutpatient',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='op_uploadedreportsfiles',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='op_uploadedreportsfiles',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='outpatient_payments',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='outpatient_payments',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='outpatient_paymenttransactions',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='outpatient_paymenttransactions',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='scanforoutpatient',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='scanforoutpatient',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='transfer_to_ip',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='transfer_to_ip',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='xrayforoutpatient',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='xrayforoutpatient',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]