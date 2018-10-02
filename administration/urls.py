from django.urls import path

from . import views

app_name = 'administration'

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.calendar, name='calendar'),
    path('add_event/', views.adding_event, name='add_event'),
    path('del_event/', views.deleting_event, name='del_event'),
    path('get_events/', views.get_events, name='get_events'),
    path('user_info/', views.user_info, name='user_info'),
    path('payment_info/', views.payments_info, name='payments_info'),
    path('payment/', views.payment, name='payment'),
]