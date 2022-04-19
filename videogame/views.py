from random import randrange
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import TopScore
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import collections
import sqlite3
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #return HttpResponse('<h1> Hola desde Django </h1>')
    return render(request, 'index.html')
def proceso(request):
    nombre = request.POST["nombre"]
    nombre = nombre.upper()
    return render(request,'proceso.html',{'name':nombre})

def datos(request):
    jugadores = TopScore.objects.all()
    return render(request,'datos.html',{'lista_jugadores':jugadores})

@csrf_exempt
def unity(request):
    sesion = {
        "id":1,
        "userId":1,
        "score":100
    }
    return JsonResponse(sesion)

@csrf_exempt
def buscaUsuario(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    nombre_jugador = body['nombre']
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''SELECT id, name, score FROM topscore WHERE name = ?'''
    rows = cur.execute(stringSQL,(nombre_jugador,))
    r = rows.fetchone()
    if r == None:
        j = '{"error":"No hay renglones"}'
    else:
        d = {}
        d["id"] = r[0]
        d["nombre"] = r[1]
        d["score"] = r[2]
        j = dumps(d)
    mydb.close()
    return HttpResponse(j, content_type="text/json-comment-filtered")

def listaUsuarios(request):
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''SELECT topscore.name, topscore.score FROM topscore'''
    rows = cur.execute(stringSQL)
    lista_salida = []
    for r in rows:
        d = {}
        d["nombre"] = r[0]
        d["score"] = r[1]
        lista_salida.append(d)
    j = dumps(lista_salida)
    mydb.close()
    return HttpResponse(j, content_type="text/json-comment-filtered")

@csrf_exempt
def unity2(request):
    lista = []
    retorno = {
    "id": 1,
    "user_id": 2,
    "username": "username",
    "country": "MXN",
    "total_score": "7:38",
    "time_played": "5:31",
    "dateCreated": "20220202:12:00:00"
    }
    lista.append(retorno)
    return JsonResponse(lista, safe=False)

def lista_party(request):
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''SELECT id, user_id, session_id, total_score, 
    time_played, date_Created FROM party'''
    rows = cur.execute(stringSQL)
    lista_salida = []
    for r in rows:
        d = {}
        d["id"] = r[0]
        d["username"] = r[1]
        d["score"] = r[3]
        lista_salida.append(d)
    j = dumps(lista_salida)
    return HttpResponse(j, content_type="text/json-comment-filtered")

@csrf_exempt
def usertopscores(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    usuario = body['user_id']
    print(usuario)
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''SELECT id, user_id, session_id, total_score, 
    time_played, date_Created FROM party WHERE user_id=?'''
    rows = cur.execute(stringSQL,(str(usuario),))
    rr = rows.fetchone()
    rows = cur.execute(stringSQL,(str(usuario),))
    if rr == None:
        j = '{"error":"No records for this user_id"}'
    else:
        lista_salida = []
        for r in rows:
            print(r)
            d = {}
            d["id"] = r[0]
            d["username"] = r[1]
            d["score"] = r[3]
            lista_salida.append(d)
        j = dumps(lista_salida)
    return HttpResponse(j, content_type="text/json-comment-filtered")

def usertopscores2(request):
    usuario = request.GET['user_id']
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''SELECT id, user_id, session_id, total_score, 
    time_played, date_Created FROM party WHERE user_id=?'''
    rows = cur.execute(stringSQL,(str(usuario),))
    rr = rows.fetchone()
    rows = cur.execute(stringSQL,(str(usuario),))
    if rr == None:
        raise Http404("user_id does not exist")
    else:
        lista_salida = []
        for r in rows:
            print(r)
            d = {}
            d["id"] = r[0]
            d["username"] = r[1]
            d["score"] = r[3]
            lista_salida.append(d)
        j = dumps(lista_salida)
    return HttpResponse(j, content_type="text/json-comment-filtered")

def main(request):
    return render(request,'main.html')

def grafica1(request):
    h_var = 'X'
    v_var = 'Y'
    data = [[h_var,v_var]]
    for i in range(0,11):
        data.append([randrange(101),randrange(101)])
    h_var_JSON = dumps(h_var)
    v_var_JSON = dumps(v_var)
    modified_data = dumps(data)
    return render(request,"grafica1.html",{'values':modified_data,\
    'h_title':h_var_JSON,'v_title':v_var_JSON})

def grafica(request):
    h_var = 'X'
    v_var = 'Y'
    data = [[h_var,v_var]]
    for i in range(0,11):
        data.append([randrange(101),randrange(101)])
    h_var_json = dumps(h_var)
    v_var_json = dumps(v_var)
    datos_json = dumps(data)
    return render(request,'grafica.html',{'values':datos_json,'h_title':h_var_json,'v_title':v_var_json})

@login_required
def privada(request):
    usuario = request.user
    print(usuario)
    return HttpResponse('Hola')
    """
    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = '''SELECT id, user_id, session_id, total_score, 
    time_played, date_Created FROM party WHERE django_user=?'''
    rows = cur.execute(stringSQL,(str(usuario),))
    rr = rows.fetchone()
    rows = cur.execute(stringSQL,(str(usuario),))
    if rr == None:
        raise Http404("user_id does not exist")
    else:
        lista_salida = []
        for r in rows:
            print(r)
            d = {}
            d["id"] = r[0]
            d["username"] = r[1]
            d["score"] = r[3]
            lista_salida.append(d)
        j = dumps(lista_salida)
    return HttpResponse(j, content_type="text/json-comment-filtered")
    """
    