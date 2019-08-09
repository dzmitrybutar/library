from django import forms
from .models import User, Book


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'pages', 'year']