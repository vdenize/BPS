from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse


def index(request):
    context = {

    }
    return render(request, 'login/homepage.html', context)


def sign_up(request):
    context = {

    }
    return render(request, 'signup/signup.html', context)


def logging_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse(''))
    else:
        return render(request, 'login/homepage.html', {})
