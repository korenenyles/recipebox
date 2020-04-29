from django.shortcuts import render

from recipe.models import Recipe

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})