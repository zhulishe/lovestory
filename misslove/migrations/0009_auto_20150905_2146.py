# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('misslove', '0008_auto_20150905_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='choose_type',
            field=models.IntegerField(default=1, verbose_name='\u677f\u5757\u9009\u62e9', choices=[(1, '\u5931\u604b'), (2, '\u6697\u604b'), (3, '\u5f02\u5730\u604b'), (4, '\u7231\u604b')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u5e03\u65f6\u95f4', editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(default=1, verbose_name='\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(verbose_name='\u6587\u7ae0\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u6587\u7ae0\u6807\u9898'),
        ),
    ]
