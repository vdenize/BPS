from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.


def index(request):
    context = {

    }
    return render(request, 'login/homepage.html', context)


def sign_up(request):
    context = {

    }
    return render(request, 'signup/signup.html', context)


def signing_up(request):
    ready = False
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    user = User.objects.create_user(username, email, password)
    first_name = request.POST.get('user_first_name')
    last_name = request.POST.get('user_last_name')
    phone_number = request.POST.get('user_number')
    birthday = request.POST.get('user_birthday')
    user_gender = request.POST.get('user_gender')
    profile = Profile(
            user=user,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            birthday=birthday,
            gender=user_gender)
    ready = True

    if ready:
        profile.save()
        return HttpResponseRedirect(reverse('login:index'))
    else:
        return HttpResponseRedirect(reverse('login:signup'))


def logging_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    auth = User.objects.get(username=username)
    user = authenticate(request, username=username, password=password)
    request.session['user'] = username
    if user is not None:
        login(request, user)
        if auth.is_superuser:
            return HttpResponseRedirect(reverse('administration:index'))
        else:
            return HttpResponseRedirect(reverse('login:dashboard'))
    else:
        return render(request, 'login/homepage.html', {})


def logging_out(request):
    del request.session['user']
    logout(request)
    return HttpResponseRedirect(reverse('login:index'))


def dashboard(request):
    username = request.session['user']
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    context = {
        'users': profile
    }
    return render(request, 'dashboard/dashboard.html', context)


def about(request):
    return render(request, 'about/about.html', {})