# Generated by Django 3.2.5 on 2021-08-11 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210811_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientmodelb',
            name='date',
            field=models.DateField(default=datetime.date(1970, 10, 19)),
        ),
    ]
