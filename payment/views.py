from django.shortcuts import render


def checkout(request):
    return render(request, 'order/checkout.html')


def success(request):
    return render(request, 'order/payment_success.html')
