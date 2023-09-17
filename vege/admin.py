from django.contrib import admin
from .models import *

class RecipeAdmin(admin.ModelAdmin):
    list_display=('recipe_name','recipe_description')
admin.site.register(Recipe,RecipeAdmin)
# Register your models here.
