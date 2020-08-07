from django.shortcuts import render
from recipebox_app.models import Author, Recipe

def index(request):
    recipe_list = Recipe.objects.all()
    return render(request, "index.html", {"recipes": recipe_list})
 

def recipe_detail_view(request, recipe_id):
    recipe_list = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipedetail.html', {"recipe": recipe_list})

def author_detail_view(request, author_id):
    author = Author.objects.filter(id= author_id).first()
    recipe = Recipe.objects.filter(author=author.id)
    return render(request, "authordetail.html", {"author": author, 'recipes': recipe})

