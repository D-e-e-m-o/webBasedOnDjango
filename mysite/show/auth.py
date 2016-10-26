#这个文件暂未使用
from django.contrib.auth.models import User
from .models import MyUser


class MyCustomBackend:
	def authenticate(self, username=None, password=None):
		try:
			user = MyUser.objects.get(username=username)
		except MyUser.DoesNotExist:
			return None
		else:
			if user.check_password(password):
				try:
					django_user = User.objects.get(username=user.username)
				except User.DoesNotExist:
					# 当在django中找不到此用户，便创建这个用户
					django_user = User(username=user.username, password=user.password)
					django_user.is_staff = False
					django_user.save()
				return django_user
			else:
				return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
