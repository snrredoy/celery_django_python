from django.shortcuts import render
from project.celery import add
from .tasks import sub

# Create your views here.
def home(request):
    result_add = add.delay(4, 4)
    result_sub = sub.delay(4, 4)
    print("Task is running in the background", result_add, result_sub)
    return render(request, 'home.html')