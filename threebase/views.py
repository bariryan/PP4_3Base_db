from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from threebase.forms import UploadForm
from threebase.models import Movie

def home(request):
    return HttpResponse("ok")

def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request, 'movies/movie.html', {'movie': movie})
    else:
        raise Http404('movie does not exsist')

def upload(request):
    if request.POST:       
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'movies/upload.html', {'form': UploadForm})