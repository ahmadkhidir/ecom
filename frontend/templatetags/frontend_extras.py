from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def product_in_user_cart(context, id):
    request = context.get("request")
    if request.user:
        user_cart = request.user.cart_set.last()
        p = user_cart.cartitem_set.filter(product_id=id)
        return True if p else False
