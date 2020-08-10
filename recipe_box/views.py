from django.shortcuts import render
from recipe_box.models import Author, Recipe

# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
    author = Author.objects.all()
    return render(request, "index.html", {"recipe": recipes, "author": author})


def post_detail(request, post_id):
    recipes = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": recipes})


def user_detail(request, author_id):
    author = Author.objects.filter(id=author_id).first()
    recipes = Recipe.objects.filter(author=author.id)
    return render(request, "user_detail.html", {"author": author, "recipes": recipes})
