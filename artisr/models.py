from django.db import models

 
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    full_name = models.TextField(null=True)
    def __str__(self):
        return self.first_name
    
    def save(self, *arg, **kwarg):
        self.full_name = self.first_name + self.last_name
        super().save(*arg, **kwarg)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    song_lyrics = models.CharField(max_length=1000000000,default="")
    def __str__(self):
        return self.name

    


    