from django.db import models

# Create your models here.
class request(models.Model):
	url = models.URLField()
	keywords = models.TextField()
	keywordscount = models.IntegerField()
	email = models.EmailField()
	datetime = models.DateTimeField(auto_now_add = True)