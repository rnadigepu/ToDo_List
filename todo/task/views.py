from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import task_list
from .forms import TaskForm

# Create your views here.
def home(request):
    task = task_list.objects.all()
    form = TaskForm()

    if request.method == "POST":
        filled_form = TaskForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        return redirect('/')


    return render(request,'home.html',{'task': task, 'form':form })

def updateTask(request, pk):
    task = task_list.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method=="POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')


    return render(request, 'update.html', {'form':form})

def delete(request,pk):
    item = task_list.objects.get(id = pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    return render(request,'delete.html', {'item': item })



