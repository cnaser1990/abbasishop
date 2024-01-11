from django.shortcuts import render
from .models import Movie
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView , TemplateView, CreateView, UpdateView, DeleteView
# Create your views here.

# list view with function
# def home_page(request):
#     movies = Movie.objects.all()
#     return render(request, 'home.html', {'movies': movies})

# def inception(request):
#     inceptions = Movie.objects.get(name='Inception (2010)')
#     return render(request, 'inception.html', {'inception': inceptions})

# list view with class

# class MovieListView(ListView):
#     model= Movie
#     template_name= 'home.html'
#     context_object_name= 'movies'

# detail view
# def detail_page(request, movie_id):
#     detail = Movie.objects.get(id=movie_id)
#     return render(request, 'movie_detail.html', {'detail': detail})

class MovieDetailView(DetailView):
    model= Movie
    template_name= 'detail.html'
    context_object_name= 'detail'

def home_page(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

# class Home(ListView):
#     model= Movie
#     template_name= 'index.html'
#     context_object_name= 'home'

class AboutView(TemplateView):
    template_name= 'about.html'
    
class MovieCreateView(CreateView):
    model= Movie
    template_name= 'movie_create.html'
    fields= ['name', 'genre', 'time']
    
class ContactUsView(TemplateView):
    template_name= 'contact.html'
    
class MovieUpdateView(UpdateView):
    model= Movie
    template_name= 'movie_edit.html'
    fields= ['name',  'genre', 'time']
    
class MovieDeleteView(DeleteView):
    model= Movie
    template_name= 'movie_delete.html'
    success_url= reverse_lazy('home')
    
