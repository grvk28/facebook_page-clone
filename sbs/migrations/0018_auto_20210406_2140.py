# Generated by Django 3.1.7 on 2021-04-06 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sbs', '0017_auto_20210405_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_art',
            field=models.ImageField(default='/media/dp.png', upload_to='channel/'),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_icon',
            field=models.ImageField(default='/media/g.png', upload_to='profile/'),
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='media/img/')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbs.about')),
                ('user', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
