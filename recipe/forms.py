from django import forms
from recipe.models import Author, Recipe

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields=['name','bio']
        #name = forms.CharField(max_length=50)
        #bio = forms.CharField(widget= forms.Textarea)

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author','time_required', 'description', 'instructions']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput)
