from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^add_book$', views.add_book),
	url(r'^book/(?P<num>\d+)$', views.book),
	url(r'^authors$', views.authors),
	url(r'^bookaddauth$', views.bookaddauth),
	url(r'^add_author$', views.add_author),
	url(r'^author/(?P<num>\d+)$', views.author),
	url(r'^authaddbook$', views.authaddbook)
]

