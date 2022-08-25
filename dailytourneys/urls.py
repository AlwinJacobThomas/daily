from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('signout', views.signout,name='signout'),
    path('postanad', views.postanad,name='postanad'),
    #path('details/<id:pk>',views.details,  name= 'details')
]
