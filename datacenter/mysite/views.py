from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
	myname = "何敏煌"
	data = [i for i in range(1, 43)]
	random.shuffle(data)
	lotto_numbers = data[0:6]
	special_number = data[6]
	return render(request, 'index.html', locals())

