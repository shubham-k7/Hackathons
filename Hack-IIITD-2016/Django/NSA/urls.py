from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^home', views.home, name='home'),
	url(r'^analyse', views.analyse, name='analyse'),
	url(r'^block', views.block, name='block'),
]