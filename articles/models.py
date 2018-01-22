from django.db import models

# Create your models here.
class Tag(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.title

class Article(models.Model):
	title = models.CharField(max_length=200)
	publish_date = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title

class Comment(models.Model):
	author = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	article = models.ForeignKey(Article)

	def __str__(self):
		return self.author


