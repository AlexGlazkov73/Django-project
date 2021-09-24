from django.views.generic import ListView, DetailView
from .models import Product
import datetime


class ProductsList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.utcnow()
        context['value1'] = None
        return context

# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'product.html'  # название шаблона будет product.html
    context_object_name = 'product'  # название объекта. в нём будет

