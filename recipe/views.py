from django.shortcuts import render

from recipe.models import Recipe, Author

# Create your views here.
def index(request):
    
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})

def author(request):
    data = Recipe.objects.all()
    return render(request, 'author.html', {'data': data})
    
def recipe(request):
    data = Recipe.objects.all()
    return render(request, 'recipe.html', {'data': data})