# Generated by Django 4.0.6 on 2022-12-07 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0028_scanforinpatient_scan_canceled_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferRoom',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('reason', models.TextField(default='', null=True)),
                ('assignroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='room.assignrooms')),
                ('from_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_room', to='room.rooms')),
                ('to_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_room', to='room.rooms')),
            ],
            options={
                'verbose_name_plural': 'TransferRoom',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]
