from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'auto_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'articles.views.show_main'),
    url(r'^all_articles/?(?P<number_page>\d+)?$', 'articles.views.show_all_articles'),
    url(r'^article_(?P<article_id>\d+)$', 'articles.views.show_article'),
    url(r'tag/(?P<filter_group>\w+)/?(?P<number_page>\d+)?', 'articles.views.filter_articles'),
]
