from django.contrib import admin
from articles.models import Tag, Article, Comment
# Register your models here.
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Comment)