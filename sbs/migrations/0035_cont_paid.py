# Generated by Django 3.1.7 on 2021-04-08 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0034_auto_20210408_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='cont',
            name='paid',
            field=models.CharField(default=6, max_length=50),
            preserve_default=False,
        ),
    ]
