from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime


class ShowManager(models.Manager):
	def basic_validator(self, data):
		errors = {}
		if len(data['title']) < 3:
			errors['name'] = "Title should be at least 3 characters"
		if Show.objects.filter(title = data['title']):
			errors['name'] = "This show already exists in our database"
		if len(data['network']) < 3:
			errors['network'] = "Network should be at least 3 characters"
		if datetime.strptime(data['date'], '%Y-%m-%d') > datetime.today():
			errors['date'] = "Invalid release date"
		if len(data['desc']) > 0 and len(data['desc']) < 10:
			errors['desc'] = "Description should be at least 10 characters"
		return errors



class Show(models.Model):
	title = models.CharField(max_length=50)
	network = models.CharField(max_length=20)
	release = models.DateField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ShowManager()

