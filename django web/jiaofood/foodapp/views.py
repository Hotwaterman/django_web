from django.shortcuts import render
from django.db.models import Q
from .models import *
from django.views.generic.list import ListView
from .models import Recipe
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import RecipeForm, IngredientFormSet, RecipeStepFormSet
# Create your views here.
def index(request):

    return render(request, 'index.html')


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = 'please input food name'
        return render(request, 'search.html', {'error_msg': error_msg})

    food_list = Food.objects.filter(name__icontains=q)
    return render(request, 'search.html', {'error_msg':error_msg, 'food_list':food_list})

class RecipeList(ListView):
    model = Recipe      

class RecipeDetail(DetailView):
    model = Recipe

class RecipeCreate(CreateView):
    model = Recipe
    form_class = RecipeForm
    
    def get(self, request, *args, **kwargs):
        self.object=None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet()
        recipe_step_form = RecipeStepFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  recipe_step_form=recipe_step_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form_is_valid = form.is_valid()
        ingredient_form = IngredientFormSet(request.POST, request.FILES)
        ingredient_form_is_valid = ingredient_form.is_valid()
        recipe_step_form = RecipeStepFormSet(request.POST, request.FILES)
        recipe_step_form_is_valid = recipe_step_form.is_valid()
        if form_is_valid and ingredient_form_is_valid and recipe_step_form_is_valid:
            return self.form_valid(form, ingredient_form, recipe_step_form)
        return self.form_invalid(form, ingredient_form, recipe_step_form)
        
        
        return super(RecipeCreate, self).post(request, *args, **kwargs)
    

    def form_valid(self, form, ingredient_form, recipe_step_form):
        """
        If all forms are valid then create a recipe with ingredients and steps
        """
        self.object = form.save()
        self.object.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        recipe_step_form.instance = self.object
        recipe_step_form.save()
        return HttpResponseRedirect(self.object.get_absolute_url())
        
    def form_invalid(self, form, ingredient_form, recipe_step_form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  recipe_step_form=recipe_step_form))
    
def custom_404_view(request):
    """
    Handles simple 404 errors
    """
    return render(request, 'jiaofood/error.html')