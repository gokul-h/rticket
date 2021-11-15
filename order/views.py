from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def checkout(request):
    return render(request, 'order/checkout.html')


@login_required(login_url='login')
def history(request):
    return render(request, 'order/history.html')
