from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def suma(request, num1, num2):
    sumar = int(num1) + int(num2)
    return HttpResponse("<b><h1>" + str(num1) + " + " +
                        str(num2) + " = " + str(sumar)+ "</h1></b>")

def resta(request, num1, num2):
    restar = int(num1) - int(num2)
    return HttpResponse("<b><h1>" + str(num1) + " - " +
                        str(num2) + " = " + str(restar)+ "</h1></b>")

def multiplicacion(request, num1, num2):
    multiplicar = int(num1) * int(num2)
    return HttpResponse("<b><h1>" + str(num1) + " * " +
                        str(num2) + " = " + str(multiplicar)+ "</h1></b>")

def dividision(request, num1, num2):
    try:
        dividir = int(num1) / int(num2)
    except ZeroDivisionError:
          return HttpResponse("<b> ¡No me dividas entre cero! </b>")
		
    return HttpResponse("<b><h1>" + str(num1) + " / " +
                        str(num2) + " = " + str(dividir)+ "</h1></b>")

def error(request):
	return HttpResponse("<b><h1>404 Not Found</h1>" +
                       "Algo has insertado mal</b>")
