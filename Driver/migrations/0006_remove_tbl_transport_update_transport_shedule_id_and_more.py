# Generated by Django 5.0.1 on 2024-04-06 00:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0005_tbl_transport_update'),
        ('User', '0002_alter_tbl_transport_request_transport_request_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_transport_update',
            name='transport_shedule_id',
        ),
        migrations.AddField(
            model_name='tbl_transport_update',
            name='transport_request_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='User.tbl_transport_request'),
            preserve_default=False,
        ),
    ]
