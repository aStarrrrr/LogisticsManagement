# Generated by Django 5.0.1 on 2024-04-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_tbl_transport_request_transport_request_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_transport_request',
            name='transport_request_rate',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
