from django.conf.urls import url
from . import views


app_name = 'show'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^djdz/', views.djdz, name='djdz'),
	url(r'^ctgyp/', views.ctgyp, name='ctgyp'),
]