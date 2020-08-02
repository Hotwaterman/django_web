from django.contrib import admin
from .models import *
# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ['ID', 'name']

admin.site.register(Food, FoodAdmin)

class IngredientsAdmin(admin.TabularInline):
    model = Ingredient
    
class RecipeStepAdmin(admin.TabularInline):
    model = RecipeStep

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientsAdmin,
        RecipeStepAdmin
    ]

admin.site.register(Recipe, RecipeAdmin)
