from django.shortcuts import render


# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'login/homepage.html', context)


def sign_up(request):
    context = {

    }
    return render(request, 'signup/signup.html', context)