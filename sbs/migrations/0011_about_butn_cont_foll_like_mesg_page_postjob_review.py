# Generated by Django 3.1.7 on 2021-04-02 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sbs', '0010_auto_20210329_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('des', models.CharField(max_length=500)),
                ('web', models.CharField(max_length=500)),
                ('comm', models.CharField(max_length=500)),
                ('inst', models.CharField(max_length=500)),
                ('twit', models.CharField(max_length=500)),
                ('offer', models.CharField(max_length=500)),
                ('tran', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='postjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dets', models.CharField(max_length=500)),
                ('loct', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=500)),
                ('msal', models.CharField(max_length=500)),
                ('styp', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=500)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbs.about')),
                ('user', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('catg', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=500)),
                ('webs', models.CharField(max_length=500)),
                ('loct', models.CharField(max_length=500)),
                ('hour', models.CharField(max_length=500)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbs.about')),
                ('user', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mesg',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('dete', models.CharField(max_length=500)),
                ('user', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbs.about')),
                ('user', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='foll',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbs.about')),
                ('user', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cont',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=500)),
                ('dete', models.CharField(max_length=500)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbs.about')),
                ('user', models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='butn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtcd', models.CharField(max_length=500)),
                ('webs', models.CharField(max_length=500)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbs.about')),
            ],
        ),
    ]
