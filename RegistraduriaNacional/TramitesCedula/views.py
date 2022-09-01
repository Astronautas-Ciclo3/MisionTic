from django.shortcuts import render

def PrimeraVez(request):
    return render(request,'TramitesCedula/PrimeraVez.html')

def Reexpedicion(request):
    return render(request,'TramitesCedula/Reexpedicion.html')


def correcionDeDatos(request):
    return render(request,'TramitesCedula/correcionDeDatos.html')


def cambioDeSexo(request):
    return render(request,'TramitesCedula/cambioDeSexo.html')
