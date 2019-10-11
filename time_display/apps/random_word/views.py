from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def random(request):
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 0
	# if 'key' in request.session:
	# 	request.session['counter'] += 1
	# 	print("WE GOT IT")
	# else:
	# 	request.session['counter'] = 1
	# 	print("WHY DONT WE WORK???????????!!!!!!!!!!!!!!!!!!")
	

	rword = get_random_string(length=14)
	context = {
		"word" : rword
	}
	return render(request, 'random_word/index.html', context)

def reset(request):
	request.session.clear()
	return redirect('/random_word')

