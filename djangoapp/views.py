from django.shortcuts import render


def all_chai(request):
    return render(request, 'djangoapp/all_chai.html')
