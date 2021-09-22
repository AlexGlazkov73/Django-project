from django.urls import path
from .views import ProductsList  # импортируем наше представление

urlpatterns = [
    path('', ProductsList.as_view()),
]