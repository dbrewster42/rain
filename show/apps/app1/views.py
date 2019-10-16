from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
	return redirect('/shows')

def shows(request):
	context = {
		"Shows" : Show.objects.all()
	}
	return render(request, 'app1/show.html', context)

def new(request):
	return render(request, 'app1/add.html')

def create(request):
	
	if request.method == "POST":
		newshow = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release=request.POST['date'], description=request.POST['desc'])
		
		newshow_id = newshow.id

	return redirect(f'/shows/{newshow_id}')

def info(request, num):
	this_show = Show.objects.get(id=num)
	context = {
		"Show" : this_show
	}
	return render(request, 'app1/info.html', context)


def edit(request, num):
	this_show = Show.objects.get(id=num)
	context = {
		"Show" : this_show
	}
	return render(request, 'app1/edit.html', context)

def update(request, num):
	print("asdlkfj")
	this_show = Show.objects.get(id=num)
	if request.method == "POST":
		this_show.title = request.POST['title']
		this_show.network = request.POST['network']
		this_show.release = request.POST['date']
		this_show.description = request.POST['desc']
		this_show.save()
		#newshow = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release=request.POST['date'], description=request.POST['desc'])
		#newshow_id = newshow.id
				
     
	return redirect(f'/shows/{num}')

def destroy(request, num):
	Show.objects.get(id=num).delete()
	return redirect('/shows')
