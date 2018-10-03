from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from administration.models import Payments
from login.models import Profile
from reservation.models import Event


def index(request):
    context = {

    }
    return render(request, 'administration/main.html', context)


def calendar(request):
    context ={

    }
    return render(request, 'administration/events.html', context)


def get_events(request):
    data_list = []
    events = Event.objects.all()
    for each in events:
        temp = {
            'title': each.title,
            'start': each.start,
            'end': each.end,
        }
        data_list.append(temp)
    return JsonResponse(data_list, safe=False)

def adding_event(request):
    title = request.GET.get('title', None)
    start = request.GET.get('start', None)
    end = request.GET.get('end', None)
    event = Event(
        title=str(title),
        start=str(start),
        end=str(end)
    )
    event.save()
    data = {
        "title": title,
        "start": start,
        "end": end
             }
    return JsonResponse(data)


def deleting_event(request):
    title = request.GET.get('title', None)
    start = request.GET.get('start', None)
    end = request.GET.get('end', None)
    event = Event.objects.get(title=title)
    event.delete()
    data = {
        "title": title,
        "start": start,
        "end": end
             }
    return JsonResponse(data)


def user_info(request):
    profile = Profile.objects.all()
    context = {
        'profiles': profile,
    }
    return render(request, 'administration/user.html', context)


def payments_info(request):
    payments = Payments.objects.all()
    context = {
        'payments': payments
    }
    return render(request, 'administration/payments.html', context)


def payment(request):
    context = {

    }
    return render(request, 'payment/paypal.html', context)


def edit(request, user_id):
    user = Profile.objects.get(pk=user_id)
    context = {
        'users': user
    }
    return render(request, 'administration/edit.html', context)


def editing_user(request, user_id):
    user_new = Profile.objects.get(pk=user_id)
    user_new.first_name = request.POST.get('user_first_name')
    user_new.last_name = request.POST.get('user_last_name')
    user_new.phone_number = request.POST.get('user_number')
    user_new.birthday = request.POST.get('user_birthday')
    user_new.save()
    return HttpResponseRedirect(reverse('administration:index'))


def deleting_user(request, user_id):
    user = Profile.objects.get(pk=user_id)
    user.delete()
    return HttpResponseRedirect(reverse('administration:index'))
