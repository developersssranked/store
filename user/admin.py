from django.contrib import admin
from .models import User
from products.admin import BasketAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username',)
    inlines=(BasketAdmin,)                               #Здесь мы делаем так, чтобы было видно корзину пользователя, когда аддмин заходит на страницу пользователя. Для этого предварительно пришлось создать еще один класс в products.admin
    