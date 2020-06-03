from django.shortcuts import render, reverse, HttpResponseRedirect
from recipe.models import Recipe, Author
from recipe.forms import AddRecipeForm, AddAuthorForm, LoginForm, NotStaffRecipeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    data = Recipe.objects.all()
    author = Author.objects.all()    
    return render(request, 'index.html', {'data': data, 'author': author})

def author(request, id):
    author = Author.objects.get(id=id)
    recipe = Recipe.objects.filter(author = author)
    favorites =  author.favorite.all()
    data = Recipe.objects.all()
    return render(request, 'author.html', {'author': author, 'recipe': recipe, 'data':data,'favorite':favorites})
    
def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe.html', {'recipe': recipe})


@login_required
def favorite(request, id):
    recipe = Recipe.objects.get(id=id)
    author = Author.objects.filter(user=request.user).first()
    author.favorite.add(recipe)
    return HttpResponseRedirect(reverse("recipe_url",args=(id,)))

@login_required
def unfavorite(request,id):
    recipe = Recipe.objects.get(id=id)
    author = Author.objects.filter(user=request.user).first()
    author.favorite.remove(recipe)
    return HttpResponseRedirect(reverse("recipe_url",args=(id,)))

@login_required
def recipe_add(request):
    html = "recipeaddform.html"
    form = AddRecipeForm()
    if request.user.is_staff:
        if request.method == "POST":
            form = AddRecipeForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse("home_url"))
    
    #options change whether they are staff or not
    if not request.user.is_staff:
        form = NotStaffRecipeForm(request.POST)
    #Matt Perry assisted me with extending this.     
        
        if request.method == "POST" and form.is_valid():
            data = form.cleaned_data
            non_staff_author = Recipe.objects.create(
                title=data['title'], 
                author=request.user.author,
                time_required=data['time_required'], 
                description=data['description'], 
                instructions=data['instructions'] 
                )

            return HttpResponseRedirect(reverse("home_url"))
        form = NotStaffRecipeForm()
    return render(request, html, {"form": form})

@login_required
def author_add(request):
    html = "authoraddform.html"
    form = AddAuthorForm()
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #matt perry assisted with this portion of extending the addauthor to include user
            new_user = User.objects.create_user(
                username=data['name'], password=data['password']
            )
            new_author = Author.objects.create(name=data['name'],bio=data['bio'],user=new_user)
            new_author.save()
            return HttpResponseRedirect(reverse('home_url'))    
    # lets the staff access new author form
    if request.user.is_staff:
        return render(request, html, {'form': form})
    return render(request, "forbidden.html")
              
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

def logoutview(request):
    if logout(request):
        return HttpResponseRedirect(reverse('home_url'))
    return render(request, 'logout.html', {})

@login_required()
def edit(request, id):
    recipe = Recipe.objects.get(id=id)
    title = recipe.title
    author = recipe.author
    date = recipe.date
    description = recipe.description
    time_required = recipe.time_required
    instructions = recipe.instructions
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.title = data['title']
            recipe.author = data['author']
            recipe.description = data['description']
            recipe.time_required = data['time_required']
            recipe.instructions = data['instructions']
            recipe.save()
            return HttpResponseRedirect(reverse('recipe_url', args=(id,)))
    form = AddRecipeForm(initial={
        'title': title,
        'author': author,
        'date': date,
        'description': description,
        'time_required': time_required,
        'instructions': instructions
    })
    return render(request, 'recipeaddform.html', {'form': form})


