from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.sign_up, name='signup'),
    path('logging_in/', views.logging_in, name='logging_in'),
    path('logging_out/', views.logging_out, name='logging_out'),
    path('signing_up/', views.signing_up, name='signing_up'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
]