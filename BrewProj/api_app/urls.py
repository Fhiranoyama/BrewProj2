from django.urls import path
from .views import Brewshopping, updel


urlpatterns = [
    path('brews/', Brewshopping.as_view()),
    path('update-item/<int:item_id>', updel.as_view()),
]
