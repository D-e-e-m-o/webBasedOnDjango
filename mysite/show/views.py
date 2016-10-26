from django.shortcuts import render, get_object_or_404
from .models import Artist, Works, MyUser
from django.utils import timezone
from .forms import SigninForm, SignupBuyerForm
from django.contrib.auth import login, logout


def index(request):
	context = {}
	works = Works.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:2]
	src = []
	for i in works:
		src.append("works/" + i.artist.name + '/' + i.workName + ".jpg")
	context['src'] = src
	return render(request, 'show/index.html', context)


#独家订制
def djdz(request, page):
	context = {}
	aritsts = Artist.objects.all()
	num = len(aritsts)
	li = ''
	#for i in range(int(num/3)+1):
	return render(request, 'show/djdz.html', context)


#传统工艺品
def ctgyp(request):
	return render(request, 'show/ctgyp.html')


#注册
def signup(request):
	return render(request, 'show/signup.html')


def signupBuyer(request):
	context = {}
	if request.method == 'POST':
		form = SignupBuyerForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			passwd = data['password']
			passwd2 = data['password2']
			if passwd == passwd2:
				username = data['name']
				email = data['email']
				phone = data['phone']
				user = MyUser(username=username, is_active=0, mail=email, phone=phone)
				user.password = user.hashed_password(passwd.encode())
				user.save()
				return render(request, 'show/signup_success.html')
			else:
				form.add_error('password2', '两次输入的密码不一致')
				context['form'] = form
		else:
			context['form'] = form
	else:
		context['form'] = SignupBuyerForm()
	return render(request, 'show/signup_buyer.html', context)

def signupSeller(request):
	context = {}
	if request.method == 'POST':
		form = SignupBuyerForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			passwd = data['password']
			passwd2 = data['password2']
			if passwd == passwd2:
				username = data['name']
				email = data['email']
				phone = data['phone']
				user = MyUser(username=username, is_active=0, mail=email, phone=phone)
				user.password = user.hashed_password(passwd.encode())
				user.save()
				return render(request, 'show/signup_success.html')
			else:
				form.add_error('password2', '两次输入的密码不一致')
				context['form'] = form
		else:
			context['form'] = form
	else:
		context['form'] = SignupBuyerForm()
	return render(request, 'show/signup_buyer.html', context)

def signin(request):
	context = {}
	if request.method == 'POST':
		form = SigninForm(request.POST)
		if form.is_valid():
			username = data['name']
			passwd = data['password']
			try:
				user = MyUser(username=username, password=passwd)
			except:
				pass
	return render(request, 'show/signin.html', context)
