from django.db import models

class News(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(max_length=300)
	visible = models.BooleanField(default=True)
	image = models.ImageField(blank=True, upload_to='images/news')
	
	def __unicode__(self):
		post = (self.title)
		return post 

class Song(models.Model):
	title = models.CharField(max_length=100)
	album = models.CharField(max_length=100)
	desc = models.CharField(max_length=200)
	
