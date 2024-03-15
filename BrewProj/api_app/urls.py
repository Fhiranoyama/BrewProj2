from django.urls import path
from .views import Brewshopping, updel


urlpatterns = [
    path('Brews/', Brewshopping.as_view()),
     path('update-item/<int:item_id>', updel.as_view()),
]
