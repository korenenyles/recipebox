from django.shortcuts import render, reverse, HttpResponseRedirect
from recipe.models import Recipe, Author
from recipe.forms import AddRecipeForm, AddAuthorForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    author = Author.objects.all()    
    return render(request, 'index.html', {'data': data, 'author': author})

def author(request, id):
    author = Author.objects.get(id=id)
    recipe = Recipe.objects.filter(author = author)
    data = Recipe.objects.all()
    return render(request, 'author.html', {'author': author, 'recipe': recipe, 'data':data})
    
def recipe(request, id):
    recipe = Recipe.objects.get(id=id)           
    return render(request, 'recipe.html', {'recipe': recipe})

@login_required
def recipe_add(request):
    html = "recipeaddform.html"
    form = AddRecipeForm()
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("home_url"))

    return render(request, html, {"form": form})

@login_required
def author_add(request):
    html = "authoraddform.html"
    form = AddAuthorForm()
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("home_url"))

    return render(request, html, {"form": form})

def loginview(request):
    html='login.html'
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            user= authenticate(request, username = data['username'], password = data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home_url'))
                )
    form = LoginForm()
    return render(request,'login.html', {'form': form})
    