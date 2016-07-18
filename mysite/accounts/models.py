from django.db import models
from show.models import Artist


class Seller(models.Model):
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	password = models.CharField(max_length=255)
	email = models.EmailField(max_length=255, unique=True)
	phone = models.CharField(max_length=11)

	def __str__(self):
		return self.artist.name


class Buyer(models.Model):
	name = models.CharField(max_length=20)
	password = models.CharField(max_length=255)
	email = models.EmailField(max_length=255, unique=True)
	phone = models.CharField(max_length=11)

	def __str__(self):
		return self.name
