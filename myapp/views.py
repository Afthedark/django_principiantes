#from django.shortcuts import render
# IMPORTANDO JSON PARA ENVIAR DATOS EN FORMATO JSON
from django.http import HttpResponse, JsonResponse

#IMPORTANDO LOS MODELOS
from .models import Project, Task

#Error 404
#from django.shortcuts import get_object_or_404

#Importando render para renderizar las vistas del html
from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Welcome to Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })    

"""
def hello(request, id): # or username parametro
    result = id + 100 * 2
    return HttpResponse("<h1>Hello %s</h1>" % result)
"""
def hello(request, username): # or username parametro
    return HttpResponse("<h1>Hello %s</h1>" % username)


def about(request):
    username = 'fazt'
    return render(request, 'about.html',{
        'username': username
    })




"""
def tasks(request, id):
    #task = Task.objects.get(id=id)  # El primer id es de la clase o model Task y el segundo es del parametro de la funcion
    task =get_object_or_404(Task, id=id) #Obtener Id o obtener 404
    return HttpResponse(f'tasks: {task.title}')
"""

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    }) 



