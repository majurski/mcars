# Generated by Django 3.2.3 on 2021-06-02 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_auto_20210602_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 2, 17, 52, 10, 251519)),
        ),
    ]
