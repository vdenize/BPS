from django.contrib.auth import authenticate, login
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
    if request.method == 'post' and 'submit' in request.POST:
        ready = False
        first_name = request.POST.get('user_first_name')
        last_name = request.POST.get('user_last_name')
        phone_number = request.POST.get('user_number')
        birthday = request.POST.get('user_birthday')
        user_gender = request.POST.get('user_gender')
        profile = Profile (
                           first_name=first_name,
                           last_name=last_name,
                           phone_number=phone_number,
                           birthday=birthday,
                           gender = user_gender
                          )
        ready = True

        if ready:
            if profile.is_standard_format():
                profile.save()
            else:
                profile.convert_to_standard_format()
                profile.save()
            return HttpResponseRedirect(reverse('login:index'))
        else:
            return HttpResponseRedirect(reverse('login:signup'))
    else:
        return HttpResponseRedirect(reverse('login:signup'))


def logging_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('reservation:reservation'))
    else:
        return render(request, 'login/homepage.html', {})
