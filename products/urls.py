

from django.urls import path
from products.views import ProductsListView, basket_add, basket_remove
app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name="index"),          #путь для всех объектов в каталоге
    path('category/<int:category_id>/', ProductsListView.as_view(), name="category"),      #путь для объектов по определенной категории
    path('page/<int:page>/', ProductsListView.as_view(), name="paginator"),           #путь для пагинации         
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
