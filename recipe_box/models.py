from django.db import models

from django.utils import timezone

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=20)
    instructions = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
