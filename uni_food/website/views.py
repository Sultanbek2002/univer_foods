from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from django.contrib import messages
import json


# Create your views here.
def index(request):
    if request.method == "POST":
        password = request.POST['password']
        if 'password' in request.COOKIES and 'data' in request.COOKIES:
            data = request.COOKIES.get('data')
            dataAll = json.loads(data)
            if password == request.COOKIES.get('password'):
                User.objects.create_user(username=dataAll['username'], first_name=dataAll['name'],
                                         last_name=dataAll['surname'],
                                         email=dataAll['email'], passwor=dataAll['password'])
                user = authenticate(request, username=dataAll['username'], password=dataAll['password'])
                login(request, user)
                return redirect('home')
            else:
                messages.error('Вы ввели неправильный код. Пожалуйсто проверьте почту!')
                return redirect('examination')
    return render(request, 'website/index.html')


def register(request):
    return render(request, 'website/register.html')


def examination(request):
    arg = ''
    for i in range(0, 6):
        arg += f'{randint(0, 10)}'
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']
        data = request.POST
        # COOKIES
        if password == re_password:
            print('password')
            if username == User.objects.filter(username=username):
                messages.error('Вы не можете добавлять, так как такой пользователь уже существует!!! ')
                return redirect('register')
            elif email == User.objects.filter(email=email):
                messages.error('Пользователь с такой почтой уже есть!! Поменяйте почту.')
                return redirect('register')
            else:
                send_mail(
                    'ITkg',
                    f'Hello {name}',
                    'setting.EMAIL_HOST_USER',
                    [email],
                    fail_silently=False
                )
                response = render(request, 'website/index.html')
                response.set_cookie('password', arg)
                response.set_cookie('data', data)
                return response
        else:
            messages.error(
                'Повторный пароль не совподает прежним паролем!! Обратите внимание они должны быть одиноковыми.')
            return redirect('register')
    else:
        return redirect('examination')
