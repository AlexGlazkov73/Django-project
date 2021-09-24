from django.urls import path
from .views import ProductsList, ProductDetail  # импортируем наше представление

urlpatterns = [
    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view())
]
