from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import razorpay
from order.models import order_info
from .models import pay_order


@login_required(login_url='login')
def checkout(request):
    oid = request.session['order_id']
    order = order_info.objects.get(order_id=oid)
    # For payment
    client = razorpay.Client(auth=("rzp_test_RyKhoqZabASgLH", "T0aRdoXZfH549caMmbbqWDj5"))
    DATA = {
        "amount": order.amount * 100,
        "currency": "INR",
        "payment_capture": '1',
    }
    username = request.user.username
    usermail = request.user.email
    payment = client.order.create(data=DATA)
    payment_order = pay_order(order_id=oid, payment_id=payment['id'])
    payment_order.save()
    del request.session['order_id']
    return render(request, 'order/checkout.html',
                  {'order_id': oid, 'payment': payment, 'amount': order.amount, 'usermail': usermail,
                   'username': username})


@csrf_exempt
@login_required(login_url='login')
def success(request):
    if request.method == "POST":
        a = request.POST
        payment_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                payment_id = val
                break
        pay = pay_order.objects.filter(payment_id=payment_id).first()
        pay.status = True
        pay.save()
    return render(request, 'order/payment_success.html')
