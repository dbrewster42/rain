from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
	context = {
		"Books": Book.objects.all(),
		
	}
	return render(request, 'author/index.html', context)

def add_book(request):
	if request.method == "POST":
		# print(request.post)
		Book.objects.create(title=request.POST['title'], desc=request.POST['description'])
		messages.add_message(request, messages.INFO, "Book added!")
	return redirect('/')

def book(request, num):
	
	u = Book.objects.get(id=num)
	a = Author.objects.all()
	ua = u.authors.all()
	# ua = ua.exclude(authors=u.authors)
	# for author in book.authors.all():
	# 	authors = authors.exclude(id = author.id)
	#authors = Authors.objects.exclude(id__in=book.authors.all())
	context = {
		"Book" : u,
		"Authors" : a,
		"This" : ua
	}
	return render(request, 'author/book.html', context)
def bookaddauth(request):
	if request.method == "POST":
		print(request.POST)
		num = request.POST['number']
		u = Book.objects.get(id=num)
		aid = request.POST['Auth']
		print(aid)
		newauth = Author.objects.get(id=aid)
		u.authors.add(newauth)
		
		messages.add_message(request, messages.INFO, "Author added!")
	return redirect('/')	

def authors(request):
	context = {
		"Authors" : Author.objects.all()
	}
	return render(request, 'author/authors.html', context)

def add_author(request):
	if request.method == "POST":
		Author.objects.create(first_name=request.POST['first'], last_name=request.POST['last'], notes=request.POST['notes'])

	return redirect('/authors')

def author(request, num):
	this_author = Author.objects.get(id=num)
	his_books = this_author.books.all()
	context = {
		"Author" : this_author,
		"Books" : Book.objects.all(),
		"AB" : his_books
	}	
	return render(request, 'author/author.html', context)
def authaddbook(request):
	if request.method == "POST":
		
		numb = request.POST['numb']
		this_author = Author.objects.get(id=numb)
		bid = request.POST['boo']
		
		newbook = Book.objects.get(id=bid)
		this_author.books.add(newbook)
	return redirect('/authors')