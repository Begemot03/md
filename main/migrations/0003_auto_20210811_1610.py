# Generated by Django 3.2.5 on 2021-08-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_clientmodelb_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientmodelb',
            name='sel',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientmodelb',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
    ]