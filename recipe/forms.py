from django import forms
from recipe.models import Author
"""
class Author(models.Model):
    name = models.CharField( max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()
"""
    

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields=['name','bio']
        #name = forms.CharField(max_length=50)
        #bio = forms.CharField(widget= forms.Textarea)

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time_required = forms.CharField(max_length=50)
    description = forms.CharField(widget = forms.Textarea)
    instructions = forms.CharField(widget = forms.Textarea)

