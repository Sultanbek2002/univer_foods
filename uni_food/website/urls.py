from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='home'),
    path('sign_up/', register, name='sign_up'),
    path('examination/', examination, name='examination'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', profile, name='profile'),
    path('login/', loginUser, name='login'),
    path('create_staff/', create_staff, name='create_staff')
]
