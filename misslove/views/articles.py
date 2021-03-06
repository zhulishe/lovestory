# coding=UTF-8
from django.shortcuts import render,redirect, get_object_or_404
from misslove.models import Article, NewUser, Comment
from django.shortcuts import render_to_response
from django.template import RequestContext
from misslove.forms import NewArticleForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def homepage(request):
	template_name = 'misslove/homepage.html'

	article_total = float(Article.objects.filter(status=1).count())
	article_data = []
	user_total = float(NewUser.objects.filter(is_active=True).count())
	user_data = []
	if article_data == 0:
		article_data = 1
	if user_total == 0:
		user_total = 1
	for i in range(1,5):
		article_data.append(round(float(Article.objects.filter(status=1).filter(choose_type=i).count())/article_total, 1))
		user_data.append(round(float(NewUser.objects.filter(is_active=True).filter(status=i).count())/user_total, 1))

	return render(request, template_name,
				  {"article_data": article_data, "user_data": user_data,})


@login_required
def new_article(request):
	template_name = 'misslove/new_article.html'
	if request.method == "POST":
		form = NewArticleForm(request.POST, request.FILES)
		if form.is_valid():
			#img_file = request.FILES['image']
			article = form.save(commit=False)
			#article.image = img_file
			article.author = request.user
			article.save()
			messages.success(request, u'发布文章成功')
			return redirect('article_detail', article_id=article.id)
	else:
		form = NewArticleForm()
	return render(request,template_name, {'form':form})


def article_catalog(request, article_type):
	template_name = 'misslove/article_catalog.html'
	limit = 10
	articles = Article.objects.filter(status=1).filter(choose_type=article_type).order_by('-created_time')
	article_type = Article.article_type[int(article_type)-1][1]
	paginator = Paginator(articles, limit)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return render_to_response(template_name,
							  {'articles': articles, 'article_type': article_type},
							  context_instance=RequestContext(request))


def article_detail(request, article_id):
	template_name = 'misslove/article_detail.html'
	article = get_object_or_404(Article, id=article_id)
	comments = article.comment_set.filter(status=1).order_by('-comment_time')
	return render_to_response(template_name,
							  {'article': article, 'comments':comments},
							  context_instance=RequestContext(request))							  


@login_required
def article_delete(request, article_id):
	article = get_object_or_404(Article, id = article_id)
	article.status = 0
	article.save()
	messages.success(request, u'成功删除文章')
	return redirect('user_info',user_id = request.user.id )


@login_required
def article_edit(request, article_id):
	article = get_object_or_404(Article, id = article_id)
	if request.method == "POST":
		form = NewArticleForm(request.POST, request.FILES, instance=article)
		if form.is_valid():
			article = form.save(commit=False)
			article.author = request.user
			article.save()
			messages.success(request, u'文章编辑成功')
			return redirect('article_detail',article_id=article_id)
	else:
		form = NewArticleForm(instance=article)
	return render(request, 'misslove/new_article.html', {'form':form})




