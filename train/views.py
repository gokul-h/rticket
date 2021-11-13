from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'train/index.html')


def about(request):
    return render(request, 'train/about.html')


def sitemap(request):
    return render(request, 'sitemap.html')


def search(request):
    return render(request, 'train/search.html')


def train_between_stations(request):
    return render(request, 'train/train_between_stations.html')


def train_info(request):
    return render(request, 'train/train_info.html')


def user_home(request):
    return render(request, 'authenticated/user_home.html')


def user_info(request):
    return render(request, 'authenticated/user_info.html')
