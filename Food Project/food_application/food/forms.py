from django import forms
from .models import Item
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','description','address','price','rating','image')

class RegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=('username','email','password1','password2')

