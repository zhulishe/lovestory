#! /usr/bin/python
# -*- coding: utf-8 -*-

from misslove.models import Article
from haystack import indexes


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')

	def get_model(self):
		return Article

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
