from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    tasks= task.objects.all()
    form= taskForm()

    if request.method == "POST":
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context= {'taskk':tasks,'form':form }
    return render(request, 'tasks/lists.html',context)

def updateTask(request, pk):
    taskss = task.objects.get(id=pk)
    form = taskForm(instance= taskss)

    if request.method == "POST":
        form = taskForm(request.POST,instance=taskss)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)

def  deleteTask(request, pk):
    item = task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')

    context={'item':item}

    return render(request, 'tasks/delete.html', context)
