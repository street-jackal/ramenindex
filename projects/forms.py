from django import forms
from projects.models import Project

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class for creating custom user signup form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=60, help_text='Required. Please enter valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# class defining what's in a ramen review entry
class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'technology', 'heat', 'rating', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'technology': forms.Select(attrs={'class': 'form-inline'}),
            'heat': forms.Select(attrs={'class': 'form-inline'}),
            'rating': forms.Select(attrs={'class': 'form-inline'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }