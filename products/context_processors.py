from products.models import Basket


def baskets(request):                     #Контекстный процессор, который делает переменную basket глобальной
    user=request.user
    return {'basket':Basket.objects.filter(user=user) if user.is_authenticated else []}
