from django.shortcuts import render, HttpResponseRedirect
from .models import Posts, category, Basket
from user.models import User


# функции=контролеры=вьюхи
# контекст=контент


def index(request):
    context = {
        'title': 'test title',
        'username': 'valeriy',
        'ispromotion': False,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store-каталог',
        'products': Posts.objects.all(),
        'categories': category.objects.all()
    }

    return render(request, 'products/products.html', context)


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


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
