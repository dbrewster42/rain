from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import random

def index(request):
	if 'gold' not in request.session:
		request.session['gold']= 0
		request.session['activities']= []
		request.session['log']= []
#dictionary
	return render(request, 'app1/index.html')

def process_money(request):
	if request.method == "POST":
		time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
		if request.POST['move']=='farm':
			num = random.randrange(10, 20)
			request.session['gold'] += num
			request.session['activities'].append(num)
						
		elif request.POST['move']=='cave':
			num = random.randrange(5, 10)
			request.session['gold'] += num
			request.session['log'].append({'result': f"Earned {num} golds from the cave! {time}", 'amount':num })

		elif request.POST['move']=='house':
			num = random.randrange(2, 5)
			request.session['gold'] += num
			request.session['activities'].append[{'result': f"Earned {num} golds from the house! {time}", 'amount':num }]

		elif request.POST['move']=='casino':
			num = random.randrange(-50, 50)
			request.session['gold'] += num
			if num < 0:
				request.session['activities'].append({'result': f"Entered a casino and lost {num} golds.. Ouch.. {time}", 'amount':num })
			elif num ==0:
				request.session['activities'].append({'result': f"Entered a casino and broke even. {time}", 'amount':num })
			else:
				request.session['activities'].append({'result': f"Entered a casino and won {num} golds! {time}", 'amount':num })

	if request.session['gold']>= 50:
		return HttpResponse("YOU WIN!!!")


	return render(request, 'app1/index.html')

def reset(request):
	request.session.clear()
	return redirect('/')


		


