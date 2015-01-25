from django.shortcuts import render
from django.http import HttpResponse

#相当于C层的方法
def index(request):
	return HttpResponse("zhuotianzhu ni jiushi ge doub!")
