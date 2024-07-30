from django.shortcuts import render, redirect
from .models import Task
from .forms import Taskform


def home(request):
    tasks = Task.objects.all()
    form = Taskform()
    
    if request.method == 'POST':
        ts = Taskform(request.POST)
        ts.save()
        return redirect('home')
    con = {'tasks':tasks,'form':form}
    return render(request,'home.html',con)

def updatetask(request,pk):
    task = Task.objects.get(id=pk)
    form = Taskform(instance=task)
    
    if request.method=='POST':
        ts = Taskform(request.POST, instance=task)
        ts.save()
        return redirect('/')
    con={'form':form}
    return render(request,'update_task.html',con)

def deletetask(request,pk):
    task = Task.objects.get(id=pk)
    
    if request.method=='POST':
        task.delete()
        return redirect('/')
    con={'task':task}
    return render(request,'delete.html',con)