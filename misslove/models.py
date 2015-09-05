# -*- coding: UTF-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class Article(models.Model):
	class Meta:
		verbose_name = u'文章'
		verbose_name_plural = u'文章'

	article_type = (
		(1, u'失恋'),
		(2, u'暗恋'),
		(3, u'异地恋'),
		(4, u'爱恋'),
	)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(u'文章标题',max_length=200)
	text = models.TextField(u'文章内容')
	choose_type = models.IntegerField(u'板块选择',choices=article_type, default=article_type[0][0])
	created_time = models.DateTimeField(u'发布时间',default=timezone.now, editable=False)
	# article valid or invalid
	status = models.IntegerField(u'状态',default=1)
	image = models.ImageField(u'文章图片',upload_to='images/articleimg', blank=True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	class Meta:
		verbose_name = u'评论'
		verbose_name_plural = u'评论'

	article = models.ForeignKey(Article)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	content = models.TextField()
	comment_time = models.DateTimeField(default=timezone.now,editable=False)
	# comment is valid or invalid
	status = models.IntegerField(default=1)

	def __unicode__(self):
		return self.article.title + '_' + self.author.username


class NewUser(AbstractUser):
	sex_choice = (
		('f', u'女'),
		('m', u'男'),
		('o', u'其他'),
	)
	love_status = (
		(1, u'失恋'),
		(2, u'暗恋'),
		(3, u'异地恋'),
		(4, u'爱恋'),
	)
	gender = models.CharField(u'性别', max_length=1, choices=sex_choice, default=sex_choice[0][0])
	whats_up = models.CharField(u'个性签名', max_length=50, default=u'这个人什么都没留下哦')
	status = models.IntegerField(u'恋爱状态', choices=love_status, default=love_status[0][0])
	avatar = models.ImageField(u'头像', upload_to='images/useravatar', blank=True)

	def get_avatar(self):
		if self.avatar and hasattr(self.avatar, 'url'):
			return self.avatar.url
		else:
			return '/media/images/useravatar/default_avatar.jpg'

	def __unicode__(self):
		return self.username
