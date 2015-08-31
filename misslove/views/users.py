from django.shortcuts import get_object_or_404,render_to_response,redirect
from django.template import RequestContext
from misslove.models import NewUser, Article, Comment
from misslove.forms import UserForm, InfoEdit
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



@login_required
def user_info(request, user_id):
	template_name = "misslove/userinfo.html"
	current_user = get_object_or_404(NewUser, id = user_id)
	user_articles = current_user.article_set.filter(status=1).order_by('created_time')[:9]
	user_comments = current_user.comment_set.filter(status=1).order_by('comment_time')[:9]
	return render_to_response(template_name,
							  {'current_user':current_user,'user_articles':user_articles,
							   'user_comments':user_comments},
							  context_instance=RequestContext(request))


def sign_up(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			user_name = request.POST.get('username', '')
			password = uf.clean_password2()
			uf.save()
			user = authenticate(username = user_name, password = password)
			if user.is_active:
				login(request, user)
			return redirect('homepage')
	else:
		uf = UserForm()
	return render_to_response('misslove/usersignup.html',
							  {'user_form':uf},
							  context_instance=RequestContext(request))


@login_required
def info_edit(request, user_id):
	user = get_object_or_404(NewUser, id = user_id)
	if request.user == user:
		if request.method == 'POST':
			ifed = InfoEdit(request.POST, request.FILES, instance=user)
			if ifed.is_valid():
				user = ifed.save()
				return redirect('user_info', user_id = user_id)
		else:
			ifed = InfoEdit(instance=user)
	else:
		return redirect('homepage')
	return render_to_response('misslove/infoedit.html',
							  {'info_form': ifed},
							  context_instance=RequestContext(request))
