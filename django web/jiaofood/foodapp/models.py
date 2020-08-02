from django.db import models
from django.utils.text import slugify

# Create your models here.
class Food(models.Model):
    ID = models.CharField('ID', primary_key=True, max_length=15)
    name = models.CharField('name', max_length=100)
    FoodGroup = models.CharField('Food Group', max_length=25)
    Calories = models.CharField('Calories', max_length=6)
    Fat = models.CharField('Fat(g)', max_length=6)
    Protein = models.CharField('Protein(g)', max_length=6)
    Carbohydrate = models.CharField('Carbohydrate(g)', max_length=6)
    Sugars = models.CharField('Sugars(g)', max_length=6)
    Fiber = models.CharField('Fiber(g)', max_length=6)

    def __str__(self):
        return self.name + ':' + self.FoodGroup + str(self.Calories) + str(self.Fat) + str(self.Protein) + str(self.Carbohydrate) + str(self.Sugars) + str(self.Fiber)

    class Meta:
        db_table = 'food'

class Recipe(models.Model):
    title = models.CharField("Title", max_length=250)
    created_datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField("Description")
    
    class Meta:
        ordering = ['-created_datetime']
        
    def __unicode__(self):
        return u'%s' % self.title
    
    def get_absolute_url(self):
        return "/recipe/%i/%s" % (self.id, slugify(self.title))
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField("Ingredient", max_length=250)
    quantity = models.FloatField("Quantity")
    units = models.CharField("Units", max_length=50, null=True, blank=True) 
    
    class Meta:
        ordering = ['name']
    
class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
    rank = models.PositiveIntegerField()
    description = models.TextField("Description")
    
    class Meta:
        ordering = ['rank']
        unique_together= ('rank', 'recipe')