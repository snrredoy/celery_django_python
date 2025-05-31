from django.shortcuts import render
from project.celery import add

# Create your views here.
def home(request):
    result = add.delay(4, 4)
    print("Task is running in the background", result)
    return render(request, 'home.html')