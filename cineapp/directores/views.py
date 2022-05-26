from django.shortcuts import render

from .models import Genero,Pelicula,Directore

def index (request):
    num_peliculas= Pelicula.objects.all().count()
    num_directores=Directore.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_peliculas': num_peliculas,
            'num_directores':num_directores
        }

    )