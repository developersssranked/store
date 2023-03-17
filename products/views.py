from django.shortcuts import  HttpResponseRedirect
from .models import Posts, category, Basket
from user.models import User
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView   #Импоритируем класс, чтобы первести наш индекс вью из функции в класс
from django.views.generic.list import ListView
from common.views import CommonContextMixin
# функции=контролеры=вьюхи
# контекст=контент

class IndexView(CommonContextMixin ,TemplateView):
    template_name='products/index.html'
    title='Store'  

  
class ProductsListView(CommonContextMixin ,ListView):
    model=Posts
    template_name='products/products.html'
    paginate_by=3
    title='Store-каталог'
    def get_queryset(self) :
        queryset=super(ProductsListView,self).get_queryset()
        category_id=self.kwargs.get('category_id')                                           #теперь все данные, которые приходят к нам через юрл(к примеру категори айди) приходят в self.kwargs, там нам и нужно с ними работать. kwargs это словарь
        return queryset.filter(category_id=category_id) if category_id else queryset


    def get_context_data(self,*,object_list=None , **kwargs):
        context=super(ProductsListView,self).get_context_data()
        
        context['categories']=category.objects.all()
        return context







@login_required
def basket_add(request, product_id):
    product = Posts.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
