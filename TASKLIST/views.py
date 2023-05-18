from django.shortcuts import render, redirect
from TASKLIST.models import *
from TASKLIST.forms import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    forms = tasklistform()
    if request.method == 'POST':
        forms = tasklistform(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/todo/')

    tasks = {'tasklist':tasklist.objects.all(), 'form':forms}


    return render(request, 'TASKLIST/TASKLIST.html', tasks)

def update_task(request, pk):
    tasks = tasklist.objects.get(id=pk)
    forms = tasklistform(instance=tasks)
    if request.method == 'POST':
        forms = tasklistform(request.POST, instance=tasks)
        if forms.is_valid():
            forms.save()
            return redirect('/todo/')

    context = {'tasklist':tasks, 'form':forms}
    return render(request, 'TASKLIST/UPDATELIST.html', context)

def delete_task(request, pk):
    item = tasklist.objects.get(id=pk)
    if request.method == 'POST':
       item.delete()
       return redirect('/todo/')

    context = {'item':item}
    return render(request, 'TASKLIST/DELETE_STATUS.html', context)

