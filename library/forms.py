from django import forms
from django.forms import ModelForm

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','subtitle','author','isbn','ddn','lcn','description','keywords']


class Old_NewBookForm(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=70)
    author = forms.CharField(max_length=50)
    isbn = forms.CharField(max_length=13)
    ddn = forms.CharField(max_length=10)
    lcn = forms.CharField(max_length=10)
    description = forms.CharField(widget=forms.Textarea)
    keywords = forms.CharField(widget=forms.Textarea)
