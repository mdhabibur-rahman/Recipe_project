from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        print(recipe_name)
        print(recipe_description)
        print(recipe_image)

        Recipe.objects.create(
             recipe_name = recipe_name,
             recipe_description =recipe_description,
             recipe_image =recipe_image ,
        )

        return redirect ('/')
    
    queryset = Recipe.objects.all() 

    # if request.method=="GET":
    #     search=request.GET.get('search')
    #     if search!=None:
    #         queryset=queryset.filter(recipe_name__icontains=search)

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {"recipes" : queryset}
    return render (request,'index.html',context)


def delete_recipe(request,id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect ('/')

def update_recipe(request,id):
    queryset = Recipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image


        queryset.save()

        return redirect ('/')

    context = {"recipes" : queryset}

    return render(request,'update_recipe.html',context)

def login_page(request):
    return render(request,'login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.create(
            first_name =  first_name,
            last_name = last_name,
            username = username,
            
        )

        user.set_password(password)
        user.save()
        return redirect('/register/')

    return render(request,'register.html')