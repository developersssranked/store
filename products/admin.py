from django.contrib import admin
from .models import Posts, category,Basket

admin.site.register(category)

@admin.register(Posts)
class ProductAdmin(admin.ModelAdmin):
    list_display=('title','price','quantity','category')
    fields=('title','description',('price','quantity'),'image','category') #Создаем поля, которые будут отображаться в каждой записи. !Если создать внутри кортежа еще один кортеж, то значения, которые внутри подкортежа будут выводиться в одну строку.
    search_fields=('title',)           #Делаем поиск внутри админки(в кортеж передаем поле, по которому будем производить поиск)
    ordering=('title',)         #Делаем сортировку по именам в алфавитном порядке




class BasketAdmin(admin.TabularInline):
    model=Basket
    fields=('user','product','created_timestamp')
    readonly_fields=('created_timestamp',)
    extra=0