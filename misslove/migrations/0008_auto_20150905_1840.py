# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misslove', '0007_auto_20150901_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='choose_type',
            field=models.IntegerField(default=1, choices=[(1, '\u5931\u604b'), (2, '\u6697\u604b'), (3, '\u5f02\u5730\u604b'), (4, '\u7231\u604b')]),
        ),
    ]
