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
  	path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('set_primary_email/', views.set_primary_email, name="set primary email"),
    path('upload_file/', views.upload_file, name='upload file'),
    path('replay_to_comment/', views.replay_to_comment, name='replay to comment'),


]
