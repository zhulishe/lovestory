__author__ = 'lisa'
from django import forms
from .models import Article


class NewArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title', 'text', 'choose_type', 'image')
