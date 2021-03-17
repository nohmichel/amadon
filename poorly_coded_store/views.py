from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    sum=0
    total=0
    for one_order in Order.objects.all():
        sum+=one_order.quantity_ordered
        total+=one_order.total_price
    charge_total = Order.objects.last().total_price
    context = {
        "all_products": Product.objects.all(),
        "charge_total": charge_total, 
        "sum": sum, 
        "total": total
    }
    return render(request, "store/checkout.html", context)

def purchase(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout')


    #try aggregation

    