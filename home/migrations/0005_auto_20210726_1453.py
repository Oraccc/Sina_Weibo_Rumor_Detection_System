# Generated by Django 3.0.9 on 2021-07-26 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('home', '0004_homepage_home_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='unverified_weibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
                ('public_time', models.DateTimeField(default=datetime.datetime.now)),
                ('img_url', models.CharField(max_length=200)),
                ('dianzan', models.IntegerField()),
                ('zhuanfa', models.IntegerField()),
                ('pinglun', models.IntegerField()),
                ('fake_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='verified_weibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
                ('public_time', models.DateTimeField(default=datetime.datetime.now)),
                ('img_url', models.CharField(max_length=200)),
                ('dianzan', models.IntegerField()),
                ('zhuanfa', models.IntegerField()),
                ('pinglun', models.IntegerField()),
                ('fake_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='HomePage',
        ),
    ]
