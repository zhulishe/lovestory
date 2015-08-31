from django.shortcuts import render
from misslove.models import Comment, Article
from django.contrib.auth.decorators import login_required
from misslove.forms import CommentAdd
from django.shortcuts import get_object_or_404,redirect

# Create your views here.


@login_required
def comment_add(request, article_id):
	form = CommentAdd(request.POST)
	if form.is_valid():
		ca = form.save(commit=False)
		ca.author = request.user
		ca.article = get_object_or_404(Article, id = article_id)
		ca.save()
		return redirect('article_detail', article_id=article_id)
	else:
		return redirect('article_detail', article_id=article_id)
