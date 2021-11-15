from django.shortcuts import render
from .models import stations, train
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def home(request):
    return render(request, 'train/index.html')


def about(request):
    return render(request, 'train/about.html')


def sitemap(request):
    return render(request, 'sitemap.html')


def search(request):
    if request.method == "POST":
        if int(request.POST['train_number']):
            print("train_number")
            train_id = request.POST['train_number']
            trains = train.objects.filter(id=train_id)
            return render(request, 'train/search.html', {'train_res': trains})
        elif int(request.POST['train_name']):
            print("train_name")
            train_id1 = request.POST['train_name']
            trains = train.objects.filter(id=train_id1)
            print(trains)
            return render(request, 'train/search.html', {'train_res': trains})

    else:
        trains = train.objects.all()
        return render(request, 'train/search.html', {'trains': trains})


def train_between_stations(request):
    rail_stations = stations.objects.all().order_by('station')
    if request.method == 'POST':
        departure = request.POST['departure']
        arrival = request.POST['arrival']
        avail_train = train.objects.filter(source=departure, destination=arrival)
        return render(request, 'train/train_between_stations.html',
                      {'stations': rail_stations, 'trains': avail_train, 'arrival': arrival, 'departure': departure})
    else:
        return render(request, 'train/train_between_stations.html', {'stations': rail_stations})


def train_info(request):
    trains = train.objects.all()
    return render(request, 'train/train_info.html', {'trains': trains})


@login_required(login_url='login')
def user_home(request):
    return render(request, 'authenticated/user_home.html')


@login_required(login_url='login')
def user_info(request):
    return render(request, 'authenticated/user_info.html')


def base(request):
    return render(request, 'base.html')


def blog(request):
    return render(request, 'train/blog.html')
