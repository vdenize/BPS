from django.shortcuts import render


# Create your views here.
def index(request):
    context = {

    }
    return render(request, '../login/homepage.html', context)


def contacts(request):
    context = {

    }
    return render(request, 'contact/contacts.html', context)