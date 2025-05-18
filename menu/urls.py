from django.urls import path
from menu import views
from .views import GetFoodList, CreateFoodList

urlpatterns = [
    path("menu/fooditem/", CreateFoodList.as_view(), name="create_food_item"),
    path( "menu/check_expiry/<int:food_item_id>/",GetFoodList.as_view(), name="get_food_item" ),
]
