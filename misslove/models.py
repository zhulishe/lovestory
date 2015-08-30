#! coding=utf-8

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


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
