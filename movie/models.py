from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True) # т.е. опциональное использование

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True) # время создания обзора будет установлено автоматом, менять время нельзя (auto_now_add)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # main_to_one отрошение таблиц; on_delete: при удалении user или movie коммент удается
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # при удалении коммента, movie и user остаются
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.text