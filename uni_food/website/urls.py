from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('sign_up/', register, name='sign_up'),
    path('examination/', examination, name='examination'),
]
