from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import razorpay


@login_required(login_url='login')
def checkout(request):
    return render(request, 'order/checkout.html')


@login_required(login_url='login')
def success(request):
    return render(request, 'order/payment_success.html')
