from django.shortcuts import render


# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'admin/index.html', context)

def calendar(request):
    context ={

    }
    return render(request, 'admin/admin.html', context)


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
