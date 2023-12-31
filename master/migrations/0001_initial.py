# Generated by Django 4.0.6 on 2023-01-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCheckupMaster',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('created_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'HealthCheckupMaster',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]
