from django.shortcuts import render


# Create your views here.
def checkout(request):
    return render(request, 'order/checkout.html')


def history(request):
    return render(request, 'order/history.html')
