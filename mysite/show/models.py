from django.db import models
from django.contrib.auth.hashers import make_password, check_password


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
	username = models.CharField("用户名", max_length=32, unique=True)
	password = models.CharField("密码", max_length=50)
	is_active = models.BooleanField("帐号是否可用", default=False)
	phone = models.CharField("电话", max_length=11)
	mail = models.EmailField("邮箱", max_length=50)
	artist_name = models.CharField("艺术家姓名", max_length=20, null=True, unique=True)
	is_artist = models.BooleanField("是否是艺术家", default=False)

	def __str__(self):
		return self.username

	def hashed_password(self, password=None):
		if not password:
			return self.password
		else:
			return make_password(password, None, 'pbkdf2_sha256')

	def check_password(self, password):
		return check_password(password, self.password)

	def change_password(self, newPasswd):
		if not newPasswd:
			return self.password
		return self.hashed_password(newPasswd)

	class Meta:
		db_table = "myuser"
