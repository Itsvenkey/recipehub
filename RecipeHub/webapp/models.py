from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# model for recipe class all info about recipe is to be stored here
    
class recipe(models.Model):
    
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE,)
    ingredients = models.TextField()
    steps = models.TextField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='recipe_images/')
    
    def __str__(self):
        return self.name
    
    
