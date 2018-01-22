from django.shortcuts import render, redirect
from django.http import HttpResponse
from articles.models import Article, Tag, Comment
from django.core.paginator import Paginator

# Create your views here.
def show_main(request):
	return redirect('/all_articles')

def article_comments(article):
	''' функция для определения количества комментариев 
	статьи'''
	count_comments = Comment.objects.filter(article = article).count()
	return count_comments

def show_all_articles(request, number_page):
	''' фукнция для отображения всех статей'''
	articles = Article.objects.all().order_by('-publish_date')
	tags = Tag.objects.all()
	
	#используем пагинацию по 10 статей на страницу
	p = Paginator(articles, 10)
	if number_page:
		page = p.page(number_page)
	else:
		page = p.page(1)

	articles_and_comments = [(article, article_comments(article)) for article in page]
	link_type = 'all_articles'
	return render(request, 'main.html', {'articles': articles_and_comments, 'page': page, 'tags':tags, 'link_type':link_type})

def show_article(request, article_id):
	''' функция для отображения конкретной статьи'''
	if request.method == 'GET':
		try:
			article_id = int(article_id)
			article = Article.objects.get(id = article_id)
			comments = Comment.objects.filter(article = article)
			#определяем есть ли предыдущая и следующая статьи
			try:
				next_article = Article.objects.get(id = article_id +1)
			except: 
				next_article = None
			try:
				previous_article = Article.objects.get(id = article_id -1)
			except: 
				previous_article = None
			return render(request, 'article.html', {'article': article, 'next': next_article, 'previous':previous_article, 'comments': comments})
		except Exception as err:
			return HttpResponse("Article not found")

	elif request.method == 'POST':
		#запрос на создание нового комментария
		name = request.POST["name"]
		comment_text = request.POST["text"]
		article_id = request.POST["article_id"]

		article = Article.objects.get(id = article_id)

		comment = Comment(author = name, text = comment_text, article = article)
		comment.save()

		return redirect('/article_{0}'.format(article_id))

def filter_articles(request, filter_group, number_page):
	''' функция для фильтрации статей по тегам'''
	tags = Tag.objects.all()
	tag = Tag.objects.get(slug = filter_group)
	articles = Article.objects.filter(tags = tag)
	
	#используем пагинацию по 10 статей на страницу
	p = Paginator(articles, 10)
	if number_page:
		page = p.page(number_page)
	else:
		page = p.page(1)
	articles_and_comments = [(article, article_comments(article)) for article in page]
	link_type = 'tag/{0}'.format(filter_group)
	return render(request, 'main.html', {'articles': articles_and_comments, 'page':page, 'tags':tags, 'link_type':link_type})
