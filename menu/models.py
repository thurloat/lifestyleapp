from django.contrib.auth.models import User
from django.db import models
import datetime

CATEGORIES = (
    ('breakfast', "Breakfast"),
    ("lunch", "Lunch"),
    ("supper", "Supper/Dinner"),
    ("snack", "Snack")
)
MOODS = (
    ("happy", "Happy"),
    ("medium", "Medium"),
    ("sad", "Sad"),
    ("depressed", "Depressed"),
)

class DietDay(models.Model):
    """One sheet of meals"""
    calorie_max = models.CharField(blank=True, max_length=100)
    notes = models.TextField(blank=True)
    mood = models.CharField(blank=False, max_length=100, choices=MOODS)
    day = models.DateField(blank=True, default=datetime.datetime.now)
    user = models.ForeignKey(User)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"%s" % self.day

class Meal(models.Model):
    """One section of the DietDay"""
    user = models.ForeignKey(User)
    day = models.ForeignKey(DietDay)
    category = models.CharField(blank=False, max_length=30 ,choices=CATEGORIES)
    title = models.CharField(blank=True, max_length=100)
    calorie_max = models.IntegerField(blank=True, null=True)
    calorie_total = models.IntegerField(blank=True, null=True)
    fruit_servings = models.IntegerField(blank=True, null=True)
    meat_servings = models.IntegerField(blank=True, null=True)
    grain_servings = models.IntegerField(blank=True, null=True)
    milk_servings = models.IntegerField(blank=True, null=True)
    water_servings = models.IntegerField(blank=True, null=True)
    oils_servings = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return u"%s, %s" % (self.category, self.title)


class MealIngredient(models.Model):
    """A single entry in each meal's ingredient list"""
    meal = models.ForeignKey(Meal)
    title = models.CharField(blank=True, max_length=100)
    calories = models.IntegerField(blank=True, null=True)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"%s, cal: %s" % (self.title, self.calories)

