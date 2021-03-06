from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """ Makes the cart content available across the whole website """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        product_count += quantity

        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
