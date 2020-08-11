from django.shortcuts import render, HttpResponseRedirect, reverse
from recipebox_app.models import Author, Recipe
from recipebox_app.forms import AddAuthor, AddRecipe

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


def add_author(request):
    if request.method == "POST": 
        form = AddAuthor(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data.get("name"), 
                bio=data.get("bio")
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddAuthor()
    return render(request, "generic_form.html", {"form": form})

def add_recipe(request):
    if request.method == "POST":
        form = AddRecipe(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get("title"),
                author=data.get("author"),
                time_required=data.get("time_required"),
                description=data.get("description"),
                instructions=data.get("instructions")
            )
            return HttpResponseRedirect(reverse("homepage"))


    form = AddRecipe()
    return render(request, "generic_form.html", {"form": form}) 



    


