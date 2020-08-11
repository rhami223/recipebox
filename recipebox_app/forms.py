from django import forms
from .models import Author


class AddRecipe(forms.Form): 
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=60)
    instructions = forms.CharField(widget=forms.Textarea)

class AddAuthor(forms.Form):
    name = forms.CharField(max_length=80)
    bio = forms.CharField(widget=forms.Textarea)