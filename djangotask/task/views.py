from django.shortcuts import render
from .models import Task
def task(request):
    tasks = Task.objects.all()
    return render(request, 'task/task.html', {'tasks': tasks})
# Create your views here.
