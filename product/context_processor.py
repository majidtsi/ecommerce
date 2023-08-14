from .models import Order_product


def get_order(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_anonymous:
        order = Order_product.objects.filter(user=request.user)
        if order:
            context["nb"] = len(order)
            context["order"] = order
        else:
            context["nb"] = 0
            context["order1"] = None
    else:
        context["nb"] = 0
        context["order1"] = None
    return context