# Generated by Django 3.1.7 on 2021-04-09 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0036_auto_20210409_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='paid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sbs.page'),
            preserve_default=False,
        ),
    ]
