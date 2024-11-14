from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    cover_image = models.ImageField(upload_to='restaurant_images/')


class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='subcategory_images/')
    parent_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='dish_images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)


