from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def addtask(request):
    return render(request, 'add.html')

def register(request):
    if request.method=='POST':
        taskname=request.POST["taskname"]
        deadline=request.POST["deadline"]
        description=request.POST["description"]
        

        userdetails=Todo(taskname=taskname,deadline=deadline,description=description)
        userdetails.save()
        #return HttpResponse('Successful')
        return render(request, 'thanks.html')
     
    else:
        print('ERROR OCCURED')

def home(request):
    tasks=Todo.objects.all()
    context={
        'tasks':tasks
    }
    return render(request, 'index.html',context)

def update(request, task_id=0):
    try:
        if task_id:
            tasks=Todo.objects.filter(id=task_id)
            context={
                'tasks':tasks
            }
            return render(request, 'update.html', context)
    except:
        return HttpResponse("USER IS NOT DELETED")

def delete(request, task_id=0):

    try:
        if task_id:
            Todo_delete=Todo.objects.get(id=task_id)
            Todo_delete.delete()
            return render(request, 'thanks.html')
            #return HttpResponse('Successful')
     
    except:
        return HttpResponse("Task IS NOT DELETED")
    
def edit(request, task_id=0):
    if request.method=='POST':
        taskname=request.POST["taskname"]
        deadline=request.POST["deadline"]
        description=request.POST["description"]
        
        tasks=Todo.objects.get(id=task_id)
        tasks.taskname=taskname
        tasks.deadline=deadline
        tasks.description=description
        tasks.save()
        #return HttpResponse('UPDATED NEW TASKS')
        return render(request, 'thanks.html')

    else:
        return HttpResponse("not enter")
        