from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, Django!')
    return render(request, 'websites/index.html')

def about(request):
    return HttpResponse('About us')

def contact(request):
    # return HttpResponse('Contact us')
    return HttpResponse('contact page')

