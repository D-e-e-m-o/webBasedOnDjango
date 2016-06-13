from django.db import models


# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Works(models.Model):
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	workName = models.CharField(max_length=50)

	def __str__(self):
		return self.workName
