from django.shortcuts import render, redirect
from .models import Tasks

# Create your views here.
def list_tasks(request):
    tasks = Tasks.objects.all()
    print(tasks)
    return render(request,'list_task.html', {"tasks":tasks})

def create_task(request):
    task = Tasks(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')