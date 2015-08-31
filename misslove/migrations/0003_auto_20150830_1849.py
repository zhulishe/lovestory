# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('misslove', '0002_article_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=-1, to='misslove.Article'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.TimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=b'images/articleimg', verbose_name='\u6587\u7ae0\u56fe\u7247', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.TimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
