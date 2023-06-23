# Generated by Django 4.0.6 on 2022-12-08 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0031_assignrooms_balance_from_op'),
        ('appointment', '0032_labtestforoutpatient_lab_canceled_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer_TO_IP',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('reason', models.TextField(default='', null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('from_op', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
                ('to_ip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.assignrooms')),
                ('to_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.rooms')),
            ],
            options={
                'verbose_name_plural': 'Transfer_TO_IP',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]