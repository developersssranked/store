from django.db import models
from user.models import User


class category(models.Model):
    title = models.CharField("Название категории", max_length=200, unique=True)
    description = models.TextField("Описание", null=True, blank=True)
    class Meta:                              #класс мета это создание доп настроек, с помощью этой мы сделали отображение в админке не POSTSS, а продукты, а также продукт в единственном числе
        verbose_name='Категория'
        verbose_name_plural='Категории'
    def __str__(self):
        return self.title


class Posts(models.Model):
    title = models.CharField("Название", max_length=256)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField("Количество", default=0)
    image = models.ImageField(
        upload_to='products_images', null=True, blank=True)
    category = models.ForeignKey(
        to=category, on_delete=models.CASCADE)
    
    
    class Meta:                              #класс мета это создание доп настроек, с помощью этой мы сделали отображение в админке не POSTSS, а продукты, а также продукт в единственном числе
        verbose_name='Продукт'
        verbose_name_plural='Продукты'



    def __str__(self):
        return (f"Продукт: {self.title}. Категория: {self.category}")



class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
    def total_quantity(self):
        return sum(basket.quantity for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    objects=BasketQuerySet.as_manager()
    def __str__(self):
        return (f"Корзина для {self.user.username}.Продукт: {self.product.title}. ")
    def sum(self):
        return self.product.price*self.quantity

    