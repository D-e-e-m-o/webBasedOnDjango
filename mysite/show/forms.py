from django import forms


class SignupBuyerForm(forms.Form):
	name = forms.CharField(label='username', max_length=40)
	password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirm', min_length=6, widget=forms.PasswordInput)
	email = forms.EmailField()


class SigninForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput)
