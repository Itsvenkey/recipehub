from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import registerForm,loginForm,addRecipeForm,editRecipeForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from .models import recipe
from django.db.models import Q

# view for home page
def home(request):
    recipes = recipe.objects.all()
    context = {'recipe':recipes}
    
    return render(request,'webapp/home.html',context=context)

# view of register page

def register(request):
    form = registerForm()
    
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request,'webapp/register.html',context=context)

# view for login page

def login(request):
    form = loginForm()
    if request.method=='POST':
        form = loginForm(request,data = request.POST)
        
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return(redirect(''))
        
    context = {'form':form}
    return render(request,'webapp/login.html',context=context)



# view for logout 

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return (redirect(''))

def details(request,pk):
    recipe_detail = recipe.objects.get(id = pk)

    context ={
        'recipe_detail':recipe_detail
    }
    return render(request,'webapp/details.html',context)


def search(request):
    query=request.GET.get('query','')
    
    results = recipe.objects.filter(
        Q(name__icontains=query)| Q(ingredients__icontains=query)
    )
    
    context = {
        "results":results,
        'query':query
    }
    return render(request,'webapp/search_result.html',context)
    
    
# view for adding recipe

@login_required(login_url='login')
def addrecipe(request):
    form = addRecipeForm()
    if request.method == 'POST':
        form = addRecipeForm(request.POST,request.FILES)
        
        if form.is_valid():
            
            form.instance.author = request.user
            image = form.cleaned_data['image']
            form.save()
            return redirect('')
    
    context = {
        'form':form
    }
    
    return render(request,'webapp/add_recipe.html',context)


# view for editing recipe

@login_required(login_url='login')
def editRecipe(request,pk):
    record = recipe.objects.get(id=pk)
    
    form = editRecipeForm(instance=record)
    
    if request.method == 'POST':
        form = editRecipeForm(request.POST,instance=record)
        
        if form.is_valid():
            form.save()
            return redirect(f'/details/{pk}')
    
    context={
        'form':form
    }
    return  render(request,'webapp/edit_recipe.html',context)


#view for delete recipe

@login_required(login_url='login')
def deleteRecipe(request,pk):
    record = recipe.objects.get(id=pk)
    if request.method =='POST':
        record.delete()
        return redirect('')
    else:
        return render(request,'webapp/delete_confirm.html',{'record':record})