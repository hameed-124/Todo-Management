from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def show(request):
    tasks= Task.objects.all()
    return render(request, 'show.html', {'tasks':tasks})

def add(request):
    if request.method == 'POST':
        title=request.POST.get ('title')
        description=request.POST.get('description')
        if title:
            Task.objects.create(title=title, description=description)
            return redirect('show')
        
    return render(request, 'add.html')


def delete(request,task_id):
    task=get_object_or_404(Task, id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('show')
    
    return render(request, 'delete.html', {'task': task})


def edit(request, task_id):
    task=get_object_or_404(Task, id=task_id)
    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show')
    
    else:
        form= TaskForm(instance=task)
    return render(request,'edit.html',{'form':form, 'task':task})
    
    
