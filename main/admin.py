from django.contrib import admin
from .models import AdvUser, Cat, Order

admin.site.register(AdvUser)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('author', 'category', 'date', 'author', 'number', 'is_active')
    fields = ('category', 'date', 'number', 'is_active')


class CatAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'created_at')
    fields = ('title', 'content', 'price', 'is_active')


admin.site.register(Order, OrderAdmin)
admin.site.register(Cat, CatAdmin)
