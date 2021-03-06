# Generated by Django 3.2.5 on 2021-07-23 12:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courier_type', models.CharField(choices=[('foot', 'Foot'), ('bike', 'Bike'), ('car', 'Car')], default='foot', max_length=4)),
                ('regions', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('current_weight', models.FloatField(default=0)),
                ('max_weight', models.IntegerField()),
                ('earnings', models.FloatField(default=0)),
            ],
        ),
    ]
