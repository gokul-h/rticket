from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from train.models import train
from .models import order_info
from django.urls import reverse
import uuid


# Create your views here.
@login_required(login_url='login')
def pre_checkout(request):
    if request.method == "POST":
        train_id = request.POST['id']
        train_val = train.objects.filter(id=train_id)
        print(train_val)
        return render(request, 'order/pre_checkout.html', {'trains': train_val})
    else:
        return HttpResponse("Error")


# To save the Order Details ad Proceed
@login_required(login_url='login')
def checkout_process(request):
    if request.method == "POST":
        order_id = uuid.uuid4().hex[:10].upper()
        username = request.user.username
        train_number = request.POST['train_number']
        departure = request.POST['departure']
        arrival = request.POST['arrival']
        amount = int(float(request.POST['total']))

        order = order_info(order_id=order_id, username=username, train_number=train_number, departure=departure,
                           arrival=arrival, amount=amount)
        order.save()
        print(order)
        return redirect(reverse('checkout'))


@login_required(login_url='login')
def history(request):
    return render(request, 'order/history.html')
