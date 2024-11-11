#Importar el path de urls
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello), #Variable username es string y se pasa como argumento
    #path('hello/<int:id>', views.hello), #Variable username es int y se pasa como argumento
    path('projects/', views.projects),
    #path('tasks/<int:id>', views.tasks),
    path('tasks/<str:name>', views.tasks),
] 


