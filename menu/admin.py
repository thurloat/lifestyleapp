from django.contrib import admin
from .models import *

class MealInline(admin.TabularInline):
    model=MealIngredient

class MealAdmin(admin.ModelAdmin):
    inlines = [MealInline,]

admin.site.register(DietDay)
admin.site.register(Meal, MealAdmin)
admin.site.register(MealIngredient)
