from .models import FoodItem
from datetime import date


def get_expired_food_item(food_item):
    return food_item.expiration_date < date.today()
