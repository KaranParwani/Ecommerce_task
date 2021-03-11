from django.contrib import admin
from items.models import items, Category, CartProduct, addtocart, Order
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['item_name', 'price', 'category']
    
class CategoryProduct(admin.ModelAdmin):
    list_display = ['cat_name', 'id']    

admin.site.register(items, AdminProduct)
admin.site.register(Category)
admin.site.register(addtocart)
admin.site.register(CartProduct)
admin.site.register(Order)