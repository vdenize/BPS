from django.urls import path

from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('calendar/', views.calendar, name='calendar')
]