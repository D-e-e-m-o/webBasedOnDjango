from django import forms
from django.contrib.auth.models import User


class SignupBuyerForm(forms.Form):
	name = forms.CharField(label='username', max_length=40)
	password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirm', min_length=6, widget=forms.PasswordInput)
	email = forms.EmailField()
	phone = forms.CharField(label='phone_number', max_length=11, min_length=11)


	def clean_name(self):
		name = self.cleaned_data['name']
		if User.objects.all().filter(username=name):
			raise forms.ValidationError("用户名已经存在")
		ban = ['admin', 'null', 'none']
		if name.lower() in ban:
			raise forms.ValidationError("用户名不合法")
		return name


class SigninForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput)
