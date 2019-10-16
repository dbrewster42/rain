from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^shows$', views.shows),
	url(r'^shows/new$', views.new),
	url(r'^shows/create$', views.create),
	url(r'^shows/(?P<num>\d+)$', views.info),
	url(r'^shows/(?P<num>\d+)/edit$', views.edit),
	url(r'^shows/(?P<num>\d+)/update$', views.update),
	url(r'^shows/(?P<num>\d+)/destroy$', views.destroy),
]