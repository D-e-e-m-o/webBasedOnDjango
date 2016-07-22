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


class ProfileBase(type):
	def __new__(cls, name, bases, attrs):
		module = attrs.pop('__module__')
		parents = [b for b in bases if isinstance(b, ProfileBase)]
		if parents:
			fields = []
			for obj_name, obj in attrs.items():
				if isinstance(obj, models.Field):
					fields.append(obj_name)
				User.add_to_class(obj_name, obj)
			UserAdmin.fieldsets = list(UserAdmin.fieldsets)
			UserAdmin.fieldsets.append((name, {'fields': fields}))
		return super(ProfileBase, cls).__new__(cls, name, bases, attrs)


class ProfileUser(object):
	__metaclass__ = ProfileBase


class ExtraInfo(ProfileUser):
	phone_number= models.CharField(max_length=11, verbose_name='手机号码')
	artiist_name = models.CharField(max_length=20, unique=True, blank=True)