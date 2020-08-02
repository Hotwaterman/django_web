from django.forms.models import inlineformset_factory, ModelForm
from .models import Recipe, Ingredient, RecipeStep

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

IngredientFormSet = inlineformset_factory(Recipe, Ingredient, exclude=('recipe',))
RecipeStepFormSet = inlineformset_factory(Recipe, RecipeStep, exclude=('recipe',))