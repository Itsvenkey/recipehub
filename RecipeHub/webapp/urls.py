from django.urls import path
from .views import home,register,login,details,search,logout,addrecipe,editRecipe,deleteRecipe

urlpatterns = [
    path('', home,name=''),
    path('register/',register, name = 'register'),
    path('login/',login,name='login'),
    path('details/<int:pk>/',details,name='details'),
    path('search/results/',search,name='search_results'),
    path('logout',logout,name='logout'),
    path('add-recipe/',addrecipe,name='add-recipe'),
    path('edit-recipe/<int:pk>',editRecipe,name='edit-recipe'),
    path('delete-recipe/<int:pk>',deleteRecipe,name='delete-recipe'),
]