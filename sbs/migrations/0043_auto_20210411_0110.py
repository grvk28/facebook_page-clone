# Generated by Django 3.1.7 on 2021-04-11 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0042_auto_20210410_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cont',
            name='pid',
            field=models.IntegerField(),
        ),
    ]
