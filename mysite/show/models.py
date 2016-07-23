from django.db import models
import hashlib


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


class MyUser(models.Model):
	username = models.CharField(u"用户名", max_length=32)
	password = models.CharField(u"密码", max_length=50)
	is_active = models.IntegerField(u"帐号是否可用")
	phone = models.CharField(u"电话", max_length=11)
	mail = models.EmailField(u"邮箱", max_length=50)

	def __str__(self):
		return self.username

	def is_authenticated(self):
		return True

	def hashed_password(self, password=None):
		if not password:
			return self.password
		else:
			return hashlib.md5(password).hexdigest()

	def check_password(self, password):
		if self.hashed_password(password) == self.password:
			return True
		return False

	class Meta:
		db_table = "myuser"
