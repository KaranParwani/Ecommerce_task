from django.shortcuts import * 
from .models import items, Category, CartProduct, addtocart
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.http import request
from items.forms import CheckoutForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# from celery.worker import request 
# import requests

# Create your views here.

class Index(View):
    
    # def post(self, request):
    #     # request.session.get('cart').clear() 
    #     product = request.POST.get('product')
        
    #     cart = request.session.get('cart')
    #     if cart:
    #         quantity = cart.get(product)
    #         if quantity:
    #             cart[product] = quantity+1
    #         else:
    #             cart[product] = 1     
    #     else:
    #         cart = {}
    #         cart[product] = 1    
    #     # print(product)
    #     request.session['cart'] = cart
    #     # print(request.session['cart'] )
    #     return redirect("/")
        
    
    def get(self, request):
        pro_duct = items.get_all_items() 
        # request.session.get('cart').clear()
        categories = Category.get_all_categories()
        # categoryID = request.GET['c']
        # if categoryID:
        #     pro_duct = items.get_all_items_by_catid()
        # else:
        #     pro_duct =  items.get_all_items()
        data = {}
        data['pro_duct'] = pro_duct
        data['categories'] = categories
        return render(request, "home.html", data)  
    
# def product(request+++


def search(request):
    query = request.GET['q']
    # query2 = request.GET['q']
    pro_duct = items.objects.filter(item_name__icontains = query)
    # pro_duct2 = items.objects.filter(price__icontains = query)
    parameters = {'pro_duct' : pro_duct }
    return render(request, "search.html", parameters)



class AddToCartView(TemplateView):
    template_name = "addtocart.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.request.session.get('cart').clear() 
        product_id = self.kwargs['pro_id']
        # print(product_id)
        product_obj = items.objects.get(id = product_id)
        print(product_obj)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            print(cart_id)
            cart_obj = addtocart.objects.get(id = cart_id) 
            this_product_in_cart = cart_obj.cartproduct_set.filter(product = product_obj)
            
            # already exists in cart
            if this_product_in_cart.exists():
                cartProduct = this_product_in_cart.last()
                cartProduct.quantity += 1
                cartProduct.subtotal += product_obj.price
                cartProduct.save()
                cart_obj.total += product_obj.price
                cart_obj.save()
            else:
                cartProduct = CartProduct.objects.create(cart = cart_obj, product = product_obj, rate = product_obj.price, quantity = 1, subtotal = product_obj.price )
                cart_obj.total += product_obj.price
                cart_obj.save()      
            # # print("-----------------old ------------------------------------")
        else:
            cart_obj = addtocart.objects.create(total = 0)
            # print("+++++++++++++++++++++New +++++++++++++++++++++++++++++++++++")
            self.request.session['cart_id'] = cart_obj.id
            cartProduct = CartProduct.objects.create(cart = cart_obj, product = product_obj, rate = product_obj.price, quantity = 1, subtotal = product_obj.price )
            cart_obj.total += product_obj.price
            cart_obj.save()
          
        return context
     
     
# def mycart(request):
#     return render(request, "my_cart.html")

#     def  get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cart_id = self.request.session.get["cart_id", None]
#         if cart_id:
#             cart = addtocart.objects.get(id = cart_id)
#         else:
#             cart = None 
#         context["cart"] = cart
#         print(cart)          
#         return context
    
class MyCartView(TemplateView):
    template_name = "my_cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart = addtocart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context
    
    
class ManageCartView(View):    
        
     def get(self, request, *args, **kwargs):
        print("manage section")
        cp_id = self.kwargs["cp_id"]
        action = request.GET.get("action")
        # print(cp_id, action)
        cp_obj = CartProduct.objects.get(id = cp_id)
        cart_obj = cp_obj.cart  
        # cart_id = request.session.get("cart_id", None)
        # if cart_id:
        #     cart2 = addtocart.objects.get(id = cart_id)
        #     if cart1 != cart2:
        #         return redirect("my_cart")
        # else:
        #     return redirect("my_cart")        
        if action == 'inc':
            cp_obj.quantity += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()
        elif action == 'dsc':
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.quantity == 0:
                cp_obj.delete()
        elif action == 'rmv':
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()
        else:
            pass
        return redirect("my_cart")   
    
# class CheckoutView(View):
    
#     def get(self, request, *args, **kwargs):
#         return redirect("checkout")    

def confirm(request):
    template = render_to_string('email_template.html', {'name' : request.user.first_name})
    
    email = EmailMessage(
        'Order Confirm !',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email]
        # reply_to=['another@example.com'],
        # headers={'Message-ID': 'foo'},
    )
    
    email.fail_silently = False
    email.send()
    return render(request, "confirm.html")

class CheckoutView(CreateView):
    template_name = "checkout.html"
    form_class = CheckoutForm
    success_url = reverse_lazy("home")

    
    def checking_user(self, request, *args,**kwargs):
        print("HELLO")
    #    user = request.user
    #    print(user)
        # if request.user.is_authenticated:
        #     print("log")
        # else:
        #     print("not")    
        return super.checking_user(request, *args, **kwargs) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = addtocart.objects.get(id = cart_id)
        else:
            cart_obj = None    
        context["cart"] = cart_obj
        return context
    
    def form_valid(self, form):
        cart_id = self.request.session.get("cart_id")
        if cart_id:
            cart_obj = addtocart.objects.get(id = cart_id)
            form.instance.cart =  cart_obj
            print(cart_obj)
            form.instance.subtotal = cart_obj.total
            form.instance.total = cart_obj.total
            #      # )
            # messages.info(request, message = 'ORDER SUCCESSFUL')
            del self.request.session["cart_id"]
            return redirect('confirm')
            
                    
        # else:  
        #     return ren    
        
        return super().form_valid(form)
    
