# Generated by Django 2.1.5 on 2020-03-21 04:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20200321_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='purchase_day',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 3, 21, 4, 10, 22, 54351, tzinfo=utc), null=True, verbose_name='购买日期'),
        ),
    ]
