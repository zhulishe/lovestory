from django.shortcuts import get_object_or_404,render_to_response
from django.template import RequestContext
from misslove.models import NewUser, Article, Comment
# Create your views here.


def user_info(request, user_id):
	template_name = "misslove/userinfo.html"
	current_user = get_object_or_404(NewUser, id = user_id)
	return render_to_response( template_name,
							  {'current_user':current_user},
							  context_instance=RequestContext(request))
