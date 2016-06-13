from django.shortcuts import render, get_object_or_404
from .models import Artist, Works


# Create your views here.
def index(request):
	context = {}
	context['works'] = Works.objects.all()
	return render(request, 'show/index.html', context)
