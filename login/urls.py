from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.sign_up, name='signup'),
    path('logging_in/', views.logging_in, name='logging_in')
]