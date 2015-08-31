# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('misslove', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('choose_type', models.IntegerField(choices=[(1, '\u5931\u604b'), (2, '\u6697\u604b'), (3, '\u5f02\u5730\u604b'), (4, '\u7231\u604b')])),
                ('created_time', models.TimeField(default=django.utils.timezone.now, editable=False)),
                ('status', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to=b'images/articleimg', verbose_name='\u6587\u7ae0\u56fe\u7247', blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('comment_time', models.TimeField(default=django.utils.timezone.now, editable=False)),
                ('status', models.IntegerField(default=1)),
                ('article', models.ForeignKey(to='misslove.Article')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
