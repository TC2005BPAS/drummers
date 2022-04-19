from unicodedata import name
from django.urls import path, include
from . import views


urlpatterns = [path('', views.index, name='index'), 
    path('proceso',views.proceso, name='proceso'),
    path('datos', views.datos, name='datos'),
    path('unity2', views.unity2, name='unity2'),
    path('lista_party', views.lista_party, name='lista_party'),
    path('usertopscores', views.usertopscores, name='usertopscores'),
    path('usertopscores2', views.usertopscores2, name='usertopscores2'),
    path('unity',views.unity, name='unity'),
    path('busca',views.buscaUsuario, name='buscaUsuario'),
    path('lista',views.listaUsuarios, name='listaUsuarios'),
    path('main',views.main, name='main'),
    path('grafica1',views.grafica1, name='grafica1'),
    path('grafica',views.grafica, name='grafica'),
    path('privada',views.privada, name='privada'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]