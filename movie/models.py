from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='movies', null=True, blank=True)
    genre = models.CharField(max_length=80)
    time = models.CharField(max_length=50)
    
    
    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)