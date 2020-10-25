from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project
from pyuploadcare.dj.forms import ImageField

class SignUpForm(UserCreationForm):

    username = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control",
                                                               "placeholder":"Username"}))
    email = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control",
                                                               "placeholder":"Email"}))
    password1 = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={"class":"form-control",
                                                               "placeholder":"Password"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={"class":"form-control",
                                                               "placeholder":"Confirm Password"}))
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2',)




class ProjectForm(forms.ModelForm):
    cover_photo = ImageField(label='')

    class Meta:
        model = Project
        fields = ('title', 'url', 'description','cover_photo', 'technologies')