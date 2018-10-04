from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('send_message/', views.send_message, name='send_message'),

]