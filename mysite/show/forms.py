from django import forms
from .models import MyUser
from captcha.fields import CaptchaField


class SignupBuyerForm(forms.Form):
	name = forms.CharField(label='username', max_length=40)
	password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirm', min_length=6, widget=forms.PasswordInput)
	email = forms.EmailField()
	phone = forms.CharField(label='phone_number', max_length=11, min_length=11)
	ca = CaptchaField()

	def clean_name(self):
		name = self.cleaned_data['name']
		if MyUser.objects.all().filter(username=name):
			raise forms.ValidationError("用户名已经存在")
		ban = ['admin', 'null', 'none']
		if name.lower() in ban:
			raise forms.ValidationError("用户名不合法")
		return name


class SignupSellerForm(forms.Form):
	name = forms.CharField(label='username', max_length=40)
	password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirm', min_length=6, widget=forms.PasswordInput)
	email = forms.EmailField()
	phone = forms.CharField(label='phone_number', max_length=11, min_length=11)
	ca = CaptchaField()

	def clean_name(self):
		name = self.cleaned_data['name']
		if MyUser.objects.all().filter(username=name):
			raise forms.ValidationError("用户名已经存在")
		ban = ['admin', 'null', 'none']
		if name.lower() in ban:
			raise forms.ValidationError("用户名不合法")
		return name


class SigninForm(forms.Form):
	username = forms.CharField(label='username')
	password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput)
