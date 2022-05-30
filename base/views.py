from binascii import Incomplete
from email import message
from pdb import post_mortem
from pickle import NONE
import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm , NewUserCreationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import datetime

# Create your views here.

def login_page(request):

    page = "login"

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request , username=username , password = password)
    
        if(user):

            login(request , user)
            return redirect ('task_list')
        
        else:

            return render(request, 'base/login_register.html' , {'error':"Invalid input" , 'context': page})

    else:

        return render(request , 'base/login_register.html' , {'context' : page})


def register_page(request):

    page = 'register'
    form = NewUserCreationForm()

    if request.method == "POST":
        form = NewUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request , "account has been successfully created")
            login(request , user)
            return redirect('task_list')
        
        else:
            messages.error(request, "form was invalid ")
            

    
    return render(request, 'base/login_register.html' , {'form': form,'context':page})


def todo(request):
    return render(request , 'base/todo.html')

@login_required(login_url="login")
def logout_page(request):
    logout(request)
    return redirect ('task_list')



@login_required(login_url='login')
def taskList(request):
    
    model = Task.objects.filter(user=request.user)
    total_task = model.count()
    complete = model.filter(complete=True).count()
    incomplete =total_task - complete
    

    search = request.GET.get('search') or ""
    date = request.GET.get('select') or ""
    today = datetime.datetime.now()

    if search:
        model = model.filter(title__icontains = search)

    if(date == "1"):
        if(model.filter(create=today)):
            print(today.date)
        

    return render(request , 'base/tasklist.html' , {'model': model ,
                                                    'total_task' : total_task , 
                                                    'complete': complete ,
                                                    'incomplete': incomplete 
                })


 
@login_required(login_url='login')
def detail_view(request , pk):

    model = Task.objects.get(pk=pk)
    return render(request , 'base/task_detail.html' , {'detail': model})




@login_required(login_url='login')
def create_task(request):

    if(request.method=='POST'):
        task = TaskForm(request.POST)
        task.instance.user = request.user
        if task.is_valid():
            task.save()

        return redirect('task_list')

    task = TaskForm()

    return render(request , 'base/create_task.html' , {'task':task})



@login_required(login_url='login')
def update_task(request, pk):

    object = get_object_or_404(Task , pk=pk)

    if(request.method=='GET'):
        task = TaskForm(instance=object)
        return render(request , 'base/update-task.html' , {'task': task})


    task = TaskForm(request.POST , instance=object)
    if(task.is_valid()):
        task.save()
    
    return redirect('task_list')



@login_required(login_url='login')
def delete_task(request,pk):
    object = get_object_or_404(Task , pk=pk)

    if(request.method=="POST"):
        object.delete()
        return redirect('task_list')

    return render(request , 'base/delete.html' , {'task':object})
    
