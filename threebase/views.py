from django.http import Http404
from django.shortcuts import render
from threebase.models import Movie

def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request, 'movies/movie.html', {'movie': movie})
    else:
        raise Http404('movie does not exsist')