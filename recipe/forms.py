from django import forms
from recipe.models import Author, Recipe

class AddAuthorForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget= forms.Textarea)

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author','time_required', 'description', 'instructions']

class NotStaffRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    time_required = forms.CharField(max_length=30)
    description = forms.CharField(widget = forms.Textarea)
    instructions = forms.CharField(widget = forms.Textarea)
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput)

