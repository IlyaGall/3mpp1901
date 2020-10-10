
from django.shortcuts import render

from django import template## добавленнение index.html
from django.http import HttpResponse


def home(request):
    return render(request, 'templates/index.html')


def  hello(request):
    #return render(request, 'templates/index2.html')
    return HttpResponse(u'Привет, Мир!!', content_type="text/plain")
	#   # return HttpResponse(u'Привет, Мир!!')
def stat(request):
    return render(request, 'templates/static_handler.html')
#def  home(request):
  # return HttpResponse(u'Привет, Мир!!', content_type="text/plain")
	#   # return HttpResponse(u'Привет, Мир!!')

# Create your views here.
