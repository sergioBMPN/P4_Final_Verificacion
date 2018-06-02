from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from .forms import formulario
from .strings_example import StringsExamples
import requests
from bs4 import BeautifulSoup
import redis
import datetime
import unicodedata


# Create your views here.
def contador(request):
    if request.method == 'POST':
        form = formulario(request.POST)
        if form.is_valid():
            pagina = form.cleaned_data['pagina']
            conector = requests.get(pagina)
            statusCode = conector.status_code

            if statusCode == 200:
                htmlText = conector.text
                html = BeautifulSoup(htmlText, "html.parser")
                entradas = html.find_all('p')
                mensaje = ""
                for entrada in entradas:
                    mensaje = mensaje + " " + entrada.getText()

                resultado = StringsExamples.count_words(mensaje)

                tiempo = datetime.datetime.now()
                dia = tiempo.day
                year = tiempo.year
                fecha_actual = str(dia) + "_" + str(year)

                bbdd = redis.Redis(host='localhost', port=6379)

                introducirBBDD(bbdd, resultado, fecha_actual)
                base_datos = consultar_contador_dia(bbdd, fecha_actual)

                form = formulario()
                fecha = "Contenido en la db del dia "+str(dia)+" del "+str(year)
                return render(request, 'contador.html', {'mensaje': resultado, 'dia': fecha ,'base_datos': base_datos,'form': form})
            else:
                form = formulario()
                return render(request, 'contador.html', {'form': form})
    else:
        form = formulario()
    return render(request, 'contador.html', {'form': form})

def introducirBBDD(bbdd, resultado, fecha_actual):
    dias = bbdd.lrange("Dias", 0, -1)
    existe = False

    for dia in dias:
        if(dia.decode("utf-8") == fecha_actual):
            existe = True

    if(not existe):
        bbdd.lpush("Dias", fecha_actual)


    for tuplas in resultado:
        dicTuplas = {}

        contador_palabra = bbdd.zscore(fecha_actual, eliminar_tildes(tuplas[0]))

        if(contador_palabra != None):
            nuevo_contador = tuplas[1] + contador_palabra
            dicTuplas[eliminar_tildes(tuplas[0])] = nuevo_contador
            bbdd.zadd(fecha_actual, **dicTuplas)
        else:
            dicTuplas[eliminar_tildes(tuplas[0])] = tuplas[1]
            bbdd.zadd(fecha_actual, **dicTuplas)


def eliminar_tildes(palabra):
    s = ''.join((c for c in unicodedata.normalize('NFD', palabra) if unicodedata.category(c) != 'Mn'))
    return s

def consultar_contador_dia(bbdd, fecha_actual):
    dias = bbdd.lrange("Dias", 0, -1)
    existe = False

    for dia in dias:
        if (dia.decode("utf-8") == fecha_actual):
            existe = True

    if(existe):
        total = bbdd.zrevrangebyscore(fecha_actual, 2000, 0, None, None, True, int)

        dicResultado = {}

        for tupla in total:
            dicResultado[tupla[0].decode("utf-8")] = tupla[1]

        return str(dicResultado)
    else:
        return "No existen datos para este dia"