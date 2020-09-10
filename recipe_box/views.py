from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recipe_box.models import Author, Recipe
from recipe_box.forms import RecipeForm, AuthorForm, LoginForm, SignupForm
# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
    author = Author.objects.all()
    return render(request, "index.html", {"recipe": recipes, "author": author})


def recipe_detail(request, post_id):
    recipes = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": recipes})

def edit_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == "POST":
        if request.user.is_active is True:
            form = RecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                recipe.title = data.get('title')
                recipe.description = data.get('description')
                recipe.time_required = data.get('time_required')
                recipe.instructions = data.get('instructions')
                recipe.save()
                
                return HttpResponseRedirect(reverse("homepage"))
    data = {
        'title': recipe.title,
        'description': recipe.description,
        'time_required': recipe.time_required,
        'instructions': recipe.instructions,
    }
    form = RecipeForm(initial=data)
    return render(request, "generic_form.html", {"form": form})


def add_favorite_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    request.user.author.favorites.add(recipe)
    return redirect('/post/' + str(recipe_id) + '/')




def user_detail(request, author_id):
    author = Author.objects.filter(id=author_id).first()
    recipes = Recipe.objects.filter(author=author.id)
    favorite_list = []
    for recipe in author.favorites.all():
        favorite_list.append(recipe.id)
    favorite_recipes = Recipe.objects.filter(id__in=favorite_list)
    return render(request, "user_detail.html", {"author": author,
                                                "recipes": recipes, 'favoriterecipes': favorite_recipes})


@login_required
def recipe_form_view(request):
    if request.method == "POST":
        if request.user.is_active is True:
            form = RecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Recipe.objects.create(
                    title=data.get('title'),
                    description=data.get('description'),
                    author=request.user.author,
                    time_required=data.get('time_required'),
                    instructions=data.get('instructions')
                )
                return HttpResponseRedirect(reverse("homepage"))
    form = RecipeForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def author_form_view(request):
    if request.method == "POST":
        if request.user.is_staff & request.user.is_active is True:
            form = AuthorForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse("homepage"))
    form = AuthorForm()
    return render(request, "generic_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"),
                                password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next",
                                                            reverse("homepage")
                                                            ))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"),
                                                password=data.get("password"))
            Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})
