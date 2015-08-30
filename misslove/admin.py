from django.contrib import admin
from .models import NewUser, Article, Comment
# Register your models here.

admin.site.register(NewUser)
admin.site.register(Article)
admin.site.register(Comment)