#! /usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from misslove.models import NewUser, Article, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404


class NewArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title', 'text', 'choose_type', 'image',)


class UserForm(UserCreationForm):
	class Meta():
		model = get_user_model()
		fields = ('username', 'email',)
		lables = {
			'username': u'用户名',
			'email': u'邮箱',
		}

class InfoEdit(forms.ModelForm):
	class Meta():
		model = get_user_model()
		fields = ('username','email', 'gender', 'whats_up', 'avatar',)


class CommentAdd(forms.ModelForm):
	class Meta():
		model = Comment
		fields = ('content', )

class ChangePasswordForm(forms.Form):
	password_current = forms.CharField(label='当前密码',widget=forms.PasswordInput)
	password_new = forms.CharField(label='新密码', widget=forms.PasswordInput)
	password_again = forms.CharField(label='重复密码', widget=forms.PasswordInput)


class LoginForm(forms.Form):
	username = forms.CharField(max_length=255, required=True)
	password = forms.CharField(widget=forms.PasswordInput, required=True)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username = username, password = password)
		if user is not None:
			if not user.is_active:
				raise forms.ValidationError(u'抱歉,您已被管理员拉黑,请联系管理员')
		else:
			raise forms.ValidationError(u'用户名与密码不匹配,请重试')
		return self.cleaned_data

	def login(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password = password)
		return user


