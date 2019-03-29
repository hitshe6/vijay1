from django.db import models
#from django.db import models

class Movie(models.Model):
    actor = models.CharField(max_length=30)
    actor_movie =  models.CharField(max_length=50)
    gener = models.CharField(max_length=30)
    movie_logo= models.CharField(max_length=100)

    def __str__(self):
         return self.actor +'-----'+ self.actor_movie

class songs(models.Model):
    movie =  models.ForeignKey(Movie , on_delete= models.CASCADE)
    file_type= models.CharField(max_length=30)
    song_name =  models.CharField(max_length=30)



