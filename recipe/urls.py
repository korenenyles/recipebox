from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, ),
    path('home/', views.index, name='home_url'),
    path('author/<int:id>/', views.author, name = 'author_url'),
    path('recipe/<int:id>/', views.recipe, name = 'recipe_url'),
    path('addauthor/', views.author_add, name = 'add_author'),
    path('addrecipe/', views.recipe_add, name = 'add_recipe'),
    path('login/', views.loginview, name='login_url'),
    path('logout/', views.logoutview, name='logout_url'),
    path('edit/<int:id>', views.edit, name='edit_url'),
    path('favorite/<int:id>/', views.favorite, name='favorite_url'),
    path('unfavorite/<int:id>/', views.unfavorite, name='unfavorite_url')
]   