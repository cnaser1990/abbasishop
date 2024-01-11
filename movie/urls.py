from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie_create/', views.MovieCreateView.as_view(), name='movie_create'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
    path('movie_edit/<int:pk>/', views.MovieUpdateView.as_view(), name='movie_update'),
    path('movie_delete/<int:pk>/', views.MovieDeleteView.as_view(), name='movie_delete'),
]
