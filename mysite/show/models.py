from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.name


class Works(models.Model):
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	workName = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.workName
