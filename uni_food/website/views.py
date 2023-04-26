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

            alldata = json.loads(data)
            print(alldata)
            if password == request.COOKIES.get('password'):
                User.objects.create_user(username=dataAll['username'], first_name=dataAll['name'],
                                         last_name=dataAll['surname'],
                                         email=dataAll['email'], password=dataAll['password'])
                user = authenticate(
                    request, username=dataAll['username'], password=dataAll['password'])
                login(request, user)
                return redirect('home')
            else:
                messages.error(
                    request, 'Вы ввели неправильный код. Пожалуйсто проверьте почту!')
            #     return redirect('examination')
    return render(request, 'website/index.html')


def register(request):

    return render(request, 'website/register.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Что-то пошло не так, повторите попытку.')
            return redirect('login')
    return render(request, 'website/login.html')


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
                messages.error(
                    request, 'Вы не можете добавлять, так как такой пользователь уже существует!!! ')
                return redirect('sign_up')
            elif email == User.objects.filter(email=email):
                messages.error(
                    request, 'Пользователь с такой почтой уже есть!! Поменяйте почту.')
                return redirect('sign_up')
            else:
                send_mail(
                    'ITkg',
                    f'Подтвердите этот код {arg} ',
                    'setting.EMAIL_HOST_USER',
                    [email],
                    fail_silently=False
                )
                response = render(request, 'website/exanmination.html')
                response.set_cookie('password', arg)
                response.set_cookie('data', json.dumps(data))
                return response
        else:
            messages.error(request,
                           'Повторный пароль не совподает прежним паролем!! Обратите внимание они должны быть одиноковыми.')
            return redirect('sign_up')
    else:
        return redirect('examination')


def profile(requests):
    return render(requests, 'website/profile.html')


def create_staff(request):
    return render(request, 'website/create_staff.html')
