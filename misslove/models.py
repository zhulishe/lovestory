# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	article_type = (
		(1,u'失恋'),
		(2,u'暗恋'),
		(3,u'异地恋'),
		(4,u'爱恋'),
	)
	author = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	text = models.TextField()
	choose_type = models.IntegerField(choices=article_type)
	created_time = models.TimeField()
	# article valid or invalid
	status = models.IntegerField()
	image = models.ImageField()

class Comment(models.Model):
	author = models.ForeignKey(User)
	content = models.TextField()
	comment_time = models.TimeField()
	# comment is valid or invalid
	status = models.IntegerField()
