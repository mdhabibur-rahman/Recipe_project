from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="media/recipe/",max_length=250,null=True,default=None)
    recipr_view_count = models.IntegerField(default=1)