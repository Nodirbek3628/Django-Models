from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from .models import Task

# Create your views here.
def create_task(request:HttpRequest)->HttpResponse:
    if request.method == 'GET':
        return render(request=request,template_name='create.html')
    else:
        form = request.POST

        new_task = Task(
            name  = form.get('name'),
            title = form.get('title'),
            description = form.get('description'),
            status = form.get('status'),
            priorty = form.get('priorty'),
            start_date = form.get('start_date'),
            due_date = form.get('due_date'),
            email = form.get('email')
        )

        new_task.save()
    

        return render(request=request,template_name='create.html')
    
def tasks(request:HttpRequest)->HttpResponse:
   tasks = Task.objects.all()

   contex = {
       "task":tasks
   }

   return render(request=request,template_name='list.html',context=contex)

def home(request:HttpRequest)->HttpResponse:
    return render(request=request,template_name='home.html')





