# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(default=b'f', max_length=1, verbose_name='\u6027\u522b', choices=[(b'f', '\u5973'), (b'm', '\u7537'), (b'o', '\u5176\u4ed6')])),
                ('whats_up', models.CharField(default='\u8fd9\u4e2a\u4eba\u4ec0\u4e48\u90fd\u6ca1\u7559\u4e0b\u54e6', max_length=50, verbose_name='\u4e2a\u6027\u7b7e\u540d')),
                ('status', models.IntegerField(default=1, verbose_name='\u604b\u7231\u72b6\u6001', choices=[(1, '\u5931\u604b'), (2, '\u6697\u604b'), (3, '\u5f02\u5730\u604b'), (4, '\u7231\u604b')])),
                ('avatar', models.ImageField(upload_to=b'images/useravatar', verbose_name='\u5934\u50cf', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('text', models.TextField(verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('choose_type', models.IntegerField(default=1, verbose_name='\u677f\u5757\u9009\u62e9', choices=[(1, '\u5931\u604b'), (2, '\u6697\u604b'), (3, '\u5f02\u5730\u604b'), (4, '\u7231\u604b')])),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u5e03\u65f6\u95f4', editable=False)),
                ('status', models.IntegerField(default=1, verbose_name='\u72b6\u6001')),
                ('image', models.ImageField(upload_to=b'images/articleimg', verbose_name='\u6587\u7ae0\u56fe\u7247', blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('comment_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('status', models.IntegerField(default=1)),
                ('article', models.ForeignKey(to='misslove.Article')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
    ]
