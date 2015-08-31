# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('misslove', '0003_auto_20150831_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
