from django.urls import path

from . import views

app_name = 'administration'

urlpatterns = [
    path('', views.index, name='index'),
    path('/calendar/', views.calendar, name='calendar')
]