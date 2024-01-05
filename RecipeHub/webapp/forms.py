from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import recipe

#registeration form 


class registerForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}),help_text='',label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}),help_text='',label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'confirm password'}),help_text='',label='')
    
    class Meta:
        model = User
        fields = ['username','password1', 'password2']

# login form
class loginForm (AuthenticationForm):
    
    username = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':'username',}),label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}),label='')
    

# form for Adding Recipe

class addRecipeForm (forms.ModelForm):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Recipe Name'}),label='')
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Recipe\'s description'}),label='')
    image= forms.ImageField(widget=forms.FileInput(attrs={'placeholder':'image'}),label='image of the recipe')
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Needed Ingredients'}),label='')
    steps = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'steps to be followed'}),label='')
   
    def clean_image(self):
        # Your validation logic goes here
        image = self.cleaned_data.get('image')
        # Validate the image, if necessary
        return image
    class Meta:
        model = recipe
        fields = ['name','description','image','ingredients','steps']
        

#form for editing recipe

class editRecipeForm(forms.ModelForm):
    class Meta:
        model = recipe
        fields = ['name','description','image','ingredients','steps']