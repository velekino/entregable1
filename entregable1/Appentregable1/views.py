from http.client import HTTPResponse
from django.shortcuts import render
from Appentregable1.models import Familiar
from django.http import HttpResponse

# Create your views here.
#def curso(request):

#    materia = Curso(nombre="Hacking", camada=99999)

#    materia.save()

#    return HttpResponse(f"Estoy guardando el primer curso: {materia.nombre}")

        
def leefamilia2(request):
    #conn = sqlite3.connect('db.sqlite3')
    #print ("Opened database successfully")
    #lista_familia = conn.execute("SELECT * FROM Appentregable1_familiar")
    lista_familia= Familiar.objects.all()
    context = {'lista_familia': lista_familia}
    
    return render(request, 'C:/Users/wakapi/Desktop/entregable1/entregable1/Appentregable1/templates/inde.html', context=context)   

