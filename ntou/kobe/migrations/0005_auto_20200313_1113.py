# Generated by Django 3.0.4 on 2020-03-13 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobe', '0004_kobepost_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kobepost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
