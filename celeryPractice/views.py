from django.shortcuts import render
from project.celery import add
from .tasks import sub
from celery.result import AsyncResult

# Create your views here.
def home(request):
    result_add = add.delay(4, 4)
    result_sub = sub.delay(4, 4)
    print("Task is running in the background", result_add, result_sub)
    return render(request, 'home.html', {'result_add': result_add, 'result_sub': result_sub})

def result(request, task_id):
    result_add = AsyncResult(task_id)
    result_sub = AsyncResult(task_id)
    return render(request, 'result.html', {'result_add': result_add, 'result_sub': result_sub})
    