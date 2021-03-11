from .models import addtocart, items, CartProduct, Order
from django import forms



class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by" , "shipping_address1","shipping_address2", 
                  "mobile", "email", "city","state" ,"ZipCode", "country" ]

        widgets = {
            'ordered_by' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'shipping_address1' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'shipping_address2' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'mobile' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'email' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'city' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'state' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'ZipCode' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'country' : forms.TextInput(attrs = {'class' : 'form-control'}),
            
        }