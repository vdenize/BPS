from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from reservation.models import Events


def index(request):
    context = {

    }
    return render(request, '../login/homepage.html', context)


def reservation(request):
    context = {

    }
    return render(request, 'reservation/reservation.html', context)


def calendar(request):
    context = {

    }
    return render(request, 'calendar/calendar.html', context)


def adding_event(request):
    title = request.GET.get('title', None)
    start = request.GET.get('start', None)
    end = request.GET.get('end', None)
    event = Events(
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
    event = Events.objects.get(title=title)
    event.delete()
    data = {
        "title": title,
        "start": start,
        "end": end
             }
    return JsonResponse(data)


def get_events(request):
    # title_list = []
    # start_list = []
    # end_list = []
    events = Events.objects.all()
    for each in events:
        # title_list.append(each.title)
        # start_list.append(each.start)
        # end_list.append(each.end)
        # data = {
        #     "titles": title_list,
        #     "starts": start_list,
        #     "ends": end_list,
        # }
    data = {
            "titles": each.title,
            "starts": each.start,
            "ends": each.end,
        }
    return JsonResponse(data)
