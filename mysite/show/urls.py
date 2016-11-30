from django.conf.urls import url
from . import views


app_name = 'show'
#独家订制，传统工艺品，注册，买家注册
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^djdz/(?P<page>[0-9]+)/$', views.djdz, name='djdz'),
	url(r'^ctgyp/$', views.ctgyp, name='ctgyp'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^signup/buyer/$', views.signupBuyer, name='signupBuyer'),
]