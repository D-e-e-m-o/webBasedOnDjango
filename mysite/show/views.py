from django.shortcuts import render, get_object_or_404
from .models import Artist, Works
from django.utils import timezone


# Create your views here.
def index(request):
	context = {}
	works = Works.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:2]
	src = []
	for i in works:
		src.append("works/" + i.artist.name + '/' + i.workName + ".jpg")
	context['src'] = src
	return render(request, 'show/index.html', context)


def djdz(request):
	return render(request, 'show/djdz.html')
