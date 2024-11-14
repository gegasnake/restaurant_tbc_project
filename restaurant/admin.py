from django.contrib import admin
from .models import *

admin.register(Restaurant, MainCategory, SubCategory, Dish, Ingredient)
