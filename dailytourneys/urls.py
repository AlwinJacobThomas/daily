from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup),
    path('signin', views.signin),
    path('signout', views.signout),
    path('postanad', views.postanad),
]
