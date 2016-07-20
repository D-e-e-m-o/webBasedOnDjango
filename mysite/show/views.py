from django.shortcuts import render, get_object_or_404
from .models import Artist, Works
from django.utils import timezone
from .forms import SigninForm, SignupBuyerForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
	context = {}
	works = Works.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:2]
	src = []
	for i in works:
		src.append("works/" + i.artist.name + '/' + i.workName + ".jpg")
	context['src'] = src
	return render(request, 'show/index.html', context)


def djdz(request, page):
	context = {}
	aritsts = Artist.objects.all()
	num = len(aritsts)
	li = ''
	for i in range(int(num/3)+1):
		pass
	return render(request, 'show/djdz.html', context)


def ctgyp(request):
	return render(request, 'show/ctgyp.html')

def signup(request):
	return render(request, 'show/signup.html')

def signupBuyer(request):
	context = {}
	context['form'] = SignupBuyerForm()
	return render(request, 'show/signup_buyer.html', context)
