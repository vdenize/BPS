from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from contact.models import Message


def contacts(request):
    context = {

    }
    return render(request, 'contact/contacts.html', context)


def send_message(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    message = Message(name=name,
                      email=email,
                      message=message)
    message.save()
    return HttpResponseRedirect(reverse('login:index'))