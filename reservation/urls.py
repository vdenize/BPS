from django.urls import path

from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('calendar/', views.calendar, name='calendar'),
    path('add_event/', views.adding_event, name='add_event'),
    path('del_event/', views.deleting_event, name='del_event'),
    path('get_events/', views.get_events, name='get_events')
]