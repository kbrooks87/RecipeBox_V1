from django import forms
from recipe_box.models import Recipe, Author


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time_required = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]

        