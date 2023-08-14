from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Product, Category, Order_product
from django.core.paginator import Paginator

def product_list(request):
    product_list = Product.objects.all()
    category = Category.objects.all()
    paginator = Paginator(product_list,3)
    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    context = {'product_list': product_list,'category':category}
    return render(request,'Product/product_list.html',context)

def product_search(request,search):
    cat = Category.objects.get(CATName=search)
    product_list = Product.objects.filter(PRDCategory=cat)
    category = Category.objects.all()
    paginator = Paginator(product_list,3)
    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    context = {'product_list': product_list,'category':category}
    return render(request,'Product/product_list.html',context)

def product_detail(request, slug):
    product_detail = get_object_or_404(Product, PRDSLug=slug)
    if request.method=='POST':
        user = request.user
        quantity = request.POST["quantity_order"]
        print(quantity)
        order=Order_product()
        order.user=user
        order.product=product_detail
        order.quantity=quantity
        order.save()

    context = {'product_detail': product_detail}
    return render(request,'Product/product_detail.html', context)

def order_pro(request):
    context = {}
    if request.method == 'POST':
        id_ord = request.POST["id_ord"]
        ord_del = get_object_or_404(Order_product, id=id_ord)
        ord_del.delete()

    order = Order_product.objects.filter(user=request.user)
    if len(order)>0:
        context["nb"] = len(order)
        context["order"] = order
    else:
        context["nb"] = 0
        context["order"] = None

    return render(request,'Order/order_product.html',context)
def add_order(request):

    user = request.user
    product = request["product_detail"]
    print(user)
    print(product)
    if request.method=='POST':

        quantity = request.POST["quantity_order"]
        print(quantity)
        order=Order_product()
        order.user=user
        order.product=product
        order.quantity=quantity
        order.save()

    context = {'product_detail': product}
    return redirect(reverse('product_detail',kwargs={'product_detail':product}))








