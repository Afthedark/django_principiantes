from django.contrib import admin
# importando los modelos
from .models import Project, Task


# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
