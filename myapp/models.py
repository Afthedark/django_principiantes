from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)


"""
El borrado en cascada en SQL es una característica que permite eliminar automáticamente 
registros relacionados cuando se elimina una fila de la tabla principal. Esto ayuda a mantener 
la integridad de la base de datos y la consistencia de los datos. 
 
Para especificar el borrado en cascada, se utiliza la cláusula ON DELETE CASCADE. Por ejemplo, 
si se elimina un cliente de la tabla Clientes, se eliminarán todas las filas que contengan el 
mismo valor de identificador de cliente. 
 

"""
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Se relaciona con foreign key de Project y se elimina en cascada 
    
     