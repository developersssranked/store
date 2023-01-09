from django.db import models
from user.models import User


class category(models.Model):
    title = models.CharField("Название категории", max_length=200, unique=True)
    description = models.TextField("Описание", null=True, blank=True)

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

    def __str__(self):
        return (f"Продукт: {self.title}. Категория: {self.category}")


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Корзина для {self.user.username}.Продукт: {self.product.title}. ")
