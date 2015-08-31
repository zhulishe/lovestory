# coding=UTF-8
from django.shortcuts import render,redirect, get_object_or_404
from misslove.models import Article, NewUser, Comment
from django.shortcuts import render_to_response
from django.template import RequestContext
from misslove.forms import NewArticleForm
from PIL import Image


# Create your views here.
def homepage(request):
	template_name = 'misslove/homepage.html'
	return render_to_response(template_name,
							  context_instance=RequestContext(request))


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
			return redirect('homepage')
	else:
		form = NewArticleForm()
	return render(request,template_name, {'form':form})


def article_crossing(request):
	articles = Article.objects.filter(choose_type = 1)#.order_by('created_time')
	template_name = 'misslove/crossing.html'
	return render(request, template_name,{'articles':articles,'article_type':article_type})


def article_crush(request):
	articles = Article.objects.filter(choose_type = 2)#.order_by('created_time')
	template_name = 'misslove/crush.html'
	return render(request, template_name,{'articles':articles})