# Generated by Django 3.2.5 on 2021-08-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_clientmodelb_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientmodelb',
            old_name='image',
            new_name='imgAfter',
        ),
        migrations.RenameField(
            model_name='clientmodelb',
            old_name='sel',
            new_name='sel1',
        ),
        migrations.AddField(
            model_name='clientmodelb',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='clientmodelb',
            name='comment1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientmodelb',
            name='comment2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientmodelb',
            name='comment3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientmodelb',
            name='imgBefore',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='clientmodelb',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='clientmodelb',
            name='sel2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientmodelb',
            name='sel3',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
