from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(reverse("user_home"))
        else:
            messages.info(request, 'Invalid credentials')
            return redirect(reverse('login'))
    else:
        return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('home'))


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User exist")
                return redirect(reverse('register'))
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email exist")
                return redirect(reverse('register'))
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User created Now Sign in!')
                return redirect(reverse('login'))
        else:
            messages.info(request, 'Password not matching')
            return redirect(reverse('register'))
    else:
        return render(request, "account/register.html")
