# Generated by Django 3.1.7 on 2021-04-08 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0032_auto_20210408_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cont',
            name='pid',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='sbs.post'),
        ),
    ]
