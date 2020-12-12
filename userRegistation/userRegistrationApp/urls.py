from django.urls import path

from . import views

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from userRegistrationApp import views

urlpatterns = [
    path('', views.index, name='index'),
  	path('adminView/', views.adminView, name='adminView'),
    path('adminView/adminAddNote/', views.adminAddNote, name='adminAddNote'),
  	path(r'^register/$',views.register,name='register'),
    path(r'^user_login/$',views.user_login,name='user_login'),


]
