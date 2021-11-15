from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from train.models import train


@login_required(login_url='login')
def checkout(request):
    if request.method == "POST":
        train_id = request.POST['id']
        train_val = train.objects.filter(id=train_id)
        return render(request, 'order/checkout.html', {'train': train_val})
    else:
        return HttpResponse("Error")


@login_required(login_url='login')
def success(request):
    return render(request, 'order/payment_success.html')
