from django.db import models
from django.utils import timezone

# Create your models here.Author model:
"""
Author Model:
    Name (CharField) -string (50)
    Bio (TextField) -string (text)

Recipe Model:

    Title (CharField) - string (30)
    Author (ForeignKey) - or link
    Description (TextField)
    Time Required (Charfield) (for example, "One hour")
    Instructions (TextField)

"""

class Author(models.Model):
    name = models.CharField( max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return self.title