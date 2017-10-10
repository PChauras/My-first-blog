from django.db import models
from django.utils import timezone

class Post(models.Model):
	#author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title


class Input_number(models.Model):
	#author = models.ForeignKey('auth.User')
	#title = models.CharField(max_length=200)
	#text = models.TextField()
	#created_date = models.DateTimeField(default=timezone.now)
	#published_date = models.DateTimeField(blank=True, null=True)
	input_x = models.DecimalField(max_digits=20,decimal_places = 2)
	calc_square = models.DecimalField(max_digits=20,decimal_places = 2)
	#calc_square = input_x * input_x

	def publish(self):
		self.calc_square = input_x * input_x
		self.save()
		
	#def __str__(self):
	#	return self.title