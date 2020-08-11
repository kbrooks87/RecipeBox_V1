from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_box.models import Author, Recipe
from recipe_box.forms import RecipeForm, AuthorForm
# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
    author = Author.objects.all()
    return render(request, "index.html", {"recipe": recipes, "author": author})


def recipe_detail(request, post_id):
    recipes = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": recipes})


def user_detail(request, author_id):
    author = Author.objects.filter(id=author_id).first()
    recipes = Recipe.objects.filter(author=author.id)
    return render(request, "user_detail.html", {"author": author,
                                                "recipes": recipes})


def recipe_form_view(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                author=data.get('author'),
                time_required=data.get('time_required'),
                instructions=data.get('instructions')
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = RecipeForm()
    return render(request, "generic_form.html", {"form": form})


def author_form_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    form = AuthorForm()
    return render(request, "generic_form.html", {"form": form})
