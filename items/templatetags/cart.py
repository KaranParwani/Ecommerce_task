from django import template

register = template.Library()


@register.filter(name = 'is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    # print(keys)
    for id in keys:
        # print(id , product.id)
        print(type(id), type(product.id))
        if int(id) == product.id:
            return True
    return False;
    #         print(keys)
    # print(product, cart)
