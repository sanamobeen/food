from django.urls import path
from menu import views
from .views import get_fooditemlist,create_food_list
urlpatterns = [
    path('menu/fooditem/',create_food_list.as_view(),name= 'create fooditem'),
    path('menu/check_expiry/<int:food_item_id>/',get_fooditemlist.as_view(),name='fooditem')
]
