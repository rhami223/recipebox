from django.db import models
from django.utils import timezone

# Create your models here.
"""
Author model:

Name (CharField)
Bio (TextField)

Recipe Model:

Title (CharField)
Author (ForeignKey)
Description (TextField)
Time Required (Charfield) (for example, "One hour")
Instructions (TextField)
"""

class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()

    def __str__(self):
        return self.name 

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=60)
    instructions = models.TextField()

    def __str__(self):
        return self.title