# Generated by Django 3.1.7 on 2021-04-07 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0026_auto_20210407_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbs.page'),
        ),
    ]
