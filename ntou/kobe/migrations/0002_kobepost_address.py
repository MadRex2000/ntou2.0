# Generated by Django 3.0.4 on 2020-03-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kobepost',
            name='address',
            field=models.GenericIPAddressField(default=False, unpack_ipv4=True),
        ),
    ]
