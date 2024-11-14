# user/urls.py
from django.urls import path
from .views import (
    RestaurantCreateView, RestaurantDetailView,
    CategoryCreateView, CategoryDetailView,
    SubcategoryCreateView, SubcategoryDetailView,
    DishCreateView, DishDetailView,
    IngredientCreateView, IngredientDetailView,
)

urlpatterns = [
    path('restaurants/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),

    path('categories/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('subcategories/', SubcategoryCreateView.as_view(), name='subcategory-create'),
    path('subcategories/<int:pk>/', SubcategoryDetailView.as_view(), name='subcategory-detail'),

    path('dishes/', DishCreateView.as_view(), name='dish-create'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish-detail'),

    path('ingredients/', IngredientCreateView.as_view(), name='ingredient-create'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient-detail'),
]
