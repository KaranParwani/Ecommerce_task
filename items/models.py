from django.db import models

# Create your models here.
   
class Category(models.Model):
    cat_name = models.CharField(max_length=20, default = "")
    
    @staticmethod 
    def get_all_categories():
        return Category.objects.all()
    
    # @staticmethod 
    # def get_all_categories_by_id(category_id):
    #     if category_id:
    #         return Category.objects.filter(category = category_id)
    #     else:
    #         return Category.get_all_categories()
        
    def __str__(self):
        return self.cat_name
    
class items(models.Model):
    item_id = models.AutoField
    item_name = models.CharField(max_length=300, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    #sub_category = models.CharField(max_length=50, default = "")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.item_name    
    
    @staticmethod
    def get_all_items():
        return items.objects.all()
    
    @staticmethod
    def get_all_items_by_catid(category_id):
        if category_id:
            return items.objects.filter(category=category_id)
        else:
            return items.get_all_items()
        
        
        

    # def __str__(self):
    #     return self.created_at 

class addtocart(models.Model):
    total = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now=True)     
    
class CartProduct(models.Model):
    cart = models.ForeignKey(addtocart, on_delete=models.CASCADE, default =6)        
    product  = models.ForeignKey(items, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default = 0)
    quantity = models.PositiveIntegerField(default = 0)
    subtotal = models.PositiveIntegerField(default = 0)
    
    def __str__(self):
         return self.product 
    
    # def __str__(self):
    #     return "Cart : " + str(self.cart.id) + " Cart Product: " + str(self.id)
    
    

class Order(models.Model):
    cart = models.OneToOneField(addtocart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address1 = models.CharField(max_length=200, default=0)
    shipping_address2 = models.CharField(max_length=200, default=0)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    city = models.CharField(max_length=50,default=0 )
    state = models.CharField(max_length=50, default=0)
    ZipCode = models.BigIntegerField(default=0)
    country = models.CharField(max_length=50, default=0)
    subtotal = models.PositiveIntegerField()
    # discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order: " + str(self.id) + "  : "  + str(self.city) + ":  " + str(self.shipping_address1) 
 