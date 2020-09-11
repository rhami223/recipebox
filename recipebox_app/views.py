from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from recipebox_app.models import Author, Recipe
from recipebox_app.forms import AddAuthor, AddRecipe, LoginForm


def index(request):
    recipe_list = Recipe.objects.all()
    return render(request, "index.html", {"recipes": recipe_list})
 

def recipe_detail_view(request, recipe_id):
    recipe_list = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipedetail.html', {"recipe": recipe_list})

def author_detail_view(request, author_id):
    wanted_author = Author.objects.filter(id=author_id).first()
    recipe = Recipe.objects.filter(author=wanted_author.id)
    fav_list = wanted_author.favorite.all()
    return render(request, "authordetail.html", {"author": wanted_author, 'recipes': recipe, "favorites": fav_list})

@login_required
def add_author(request):
    if request.user.is_staff:
        if request.method == "POST": 
            form = AddAuthor(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
                Author.objects.create(
                    name=data.get("username"), 
                    bio=data.get("bio"),
                    user=new_user
                )
                login(request, new_user)
                return HttpResponseRedirect(reverse("homepage"))
    else:
        return render(request, "noaccess.html")

    form = AddAuthor()
    return render(request, "generic_form.html", {"form": form})

@login_required
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
            return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))


    form = AddRecipe()
    return render(request, "generic_form.html", {"form": form}) 

@login_required
def edit_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.user.is_staff or request.user.author.id == recipe.author.id:
        if request.method == "POST":
            form = AddRecipe(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                recipe.title=data["title"]
                recipe.author=data["author"]
                recipe.time_required=data["time_required"]
                recipe.description=data["description"]
                recipe.instructions=data["instructions"]
                recipe.save()
                return HttpResponseRedirect(reverse('recipe_detail_view', args=[recipe.id]))
        data = {
            "title": recipe.title,
            "author": recipe.author,
            "time_required": recipe.time_required,
            "description": recipe.description,
            "instructions": recipe.instructions

        }
        form = AddRecipe(initial=data)
        return render(request, "generic_form.html", {"form": form})
    return HttpResponseRedirect(reverse('homepage', args=[recipe.id]))
    


def favorite_view(request, fav_id):
    current_author = Author.objects.filter(user__id=request.user.id).first()
    add_fav_recipe = Recipe.objects.filter(id=fav_id).first()
    current_author.favorite.add(add_fav_recipe)
    current_author.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def unfavorite_view(request, unfav_id):
    current_author = Author.objects.filter(user__id=request.user.id).first()
    un_fav_recipe = Recipe.objects.filter(id=unfav_id).first()
    current_author.favorite.remove(un_fav_recipe)
    current_author.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"),password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage"))
                )

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)    
    return HttpResponseRedirect(reverse("homepage"))

    


