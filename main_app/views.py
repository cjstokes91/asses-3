from django.shortcuts import render

from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('Wish List')

def add(request):
    return render(request, 'add.html')
    

# Create your views here.
