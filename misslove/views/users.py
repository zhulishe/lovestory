# coding:UTF-8
from django.shortcuts import get_object_or_404,render_to_response,redirect
from django.template import RequestContext
from misslove.models import NewUser, Article, Comment
from misslove.forms import UserForm, InfoEdit, ChangePasswordForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth


def user_login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.login()
			if user:
				login(request, user)
				messages.success(request, u'成功登录')
				return redirect('homepage')
	else:
		form = LoginForm()
	return render_to_response('misslove/user_login.html',
							  {'form': form,},
							  context_instance=RequestContext(request))


@login_required
def user_logout(request):
	auth.logout(request)
	messages.success(request, u'成功退出')
	return redirect('homepage')


@login_required
def user_info(request, user_id):
	template_name = "misslove/user_info.html"
	current_user = get_object_or_404(NewUser, id = user_id)
	user_articles = current_user.article_set.filter(status=1).order_by('created_time')[:9]
	user_comments = current_user.comment_set.filter(status=1).order_by('comment_time')[:9]
	return render_to_response(template_name,
							  {'current_user':current_user,'user_articles':user_articles,
							   'user_comments':user_comments},
							  context_instance=RequestContext(request))


def user_signup(request):
	template_name = "misslove/user_signup.html"
	if request.method == "POST":
		uf = UserForm(request.POST)
		if uf.is_valid():
			user_name = request.POST.get('username')
			password = uf.clean_password2()
			uf.save()
			user = authenticate(username = user_name, password = password)
			if user.is_active:
				login(request,user)
				messages.add_message(u'注册成功并登录')
			return redirect('homepage')
	else:
		uf = UserForm
	return render_to_response(template_name,
							  {'user_form':uf },
							  context_instance=RequestContext(request))


@login_required
def info_edit(request, user_id):
	user = get_object_or_404(NewUser, id = user_id)
	if request.user == user:
		if request.method == 'POST':
			ifed = InfoEdit(request.POST, request.FILES, instance=user)
			if ifed.is_valid():
				user = ifed.save()
				messages.success(request, u'资料修改成功')
				return redirect('user_info', user_id = user_id)
		else:
			ifed = InfoEdit(instance=user)
	else:
		return redirect('homepage')
	return render_to_response('misslove/infoedit.html',
							  {'info_form': ifed, 'current_user':user},
							  context_instance=RequestContext(request))


@login_required
def change_password(request, user_id):
	error = []
	user = get_object_or_404(NewUser, id = user_id)
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(username=user.username,password=data['password_current'])
			if user is not None:
				if data['password_new'] == data['password_again']:
					user = get_object_or_404(NewUser, id = user_id)
					user.set_password(data['password_new'])
					user.save()
					messages.success(request, u'密码修改成功')
					return redirect('login')
				else:
					error.append("两次输入密码不一样")
			else:
				error.append("请输入正确的旧密码")
	else:
		form = ChangePasswordForm()
	return render_to_response('misslove/change_password.html',{'form':form,'error':error},
							  context_instance=RequestContext(request))

