import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem

def home(request):
    return render(request,'Home.html',locals())

def todoappVeiw(request):
    all_todo_items=TodoListItem.objects.all()
    return render(request,'todolist.html',{'all_items':all_todo_items})

def addTodoVeiw(reguest):
    x = reguest.POST['content']
    new_items = TodoListItem(content=x)
    new_items.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoVeiw(request,i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 
