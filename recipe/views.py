from django.shortcuts import render

from recipe.models import Recipe, Author

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})

def author(request, id):
    author = Author.objects.get(id=id)
    recipe = Recipe.objects.filter(author = author)
    data = Recipe.objects.all()
    return render(request, 'author.html', {'author': author, 'recipe': recipe, 'data':data})
    
def recipe(request, id):
    author = Author.objects.get(id=id)
    recipe = Recipe.objects.get(id=id)
    
    return render(request, 'recipe.html', {'recipe': recipe, 'author': author})