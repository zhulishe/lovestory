# coding:UTF-8
from django.shortcuts import render
from misslove.models import Comment, Article
from django.contrib.auth.decorators import login_required
from misslove.forms import CommentAdd
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages

# Create your views here.


@login_required
def comment_add(request, article_id):
	form = CommentAdd(request.POST)
	if form.is_valid():
		ca = form.save(commit=False)
		ca.author = request.user
		ca.article = get_object_or_404(Article, id = article_id)
		ca.save()
		messages.success(request, u'评论添加成功')
		return redirect('article_detail', article_id=article_id)
	else:
		return redirect('article_detail', article_id=article_id)


@login_required
def comment_delete(request, comment_id):
	#article = get_object_or_404(Article, id = article_id)
	comment = get_object_or_404(Comment, id = comment_id)
	comment.status = 0
	comment.save()
	messages.success(request, u'评论删除成功')
	return redirect('user_info',user_id = request.user.id)


@login_required
def comment_edit(request, comment_id):
	comment = get_object_or_404(Comment, id = comment_id)
	if request.method == 'POST':
		form = CommentAdd(request.POST, instance= comment)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.author = request.user
			comment.save()
			messages.success(request, u'评论编辑成功')
			return redirect('article_detail', article_id = comment.article.id)
	else:
		form = CommentAdd(instance=comment)
	return render(request,'misslove/edit_comment.html', {'form':form})