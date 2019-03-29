#from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def index(request):
    all_movies = Movie.objects.all()
    for a in all_movies:
        url = '/movie1/'+ str(a.id) + '/'
        html = '<a href =" '+ url + '"> ' + a.actor + '</a><br>'

    return HttpResponse(html)
def detail(request,movie_id):
    return HttpResponse("<h1>welcome in id :" +str(movie_id) + "</h1>" )

