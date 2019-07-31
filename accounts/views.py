from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Inputform

def home(request): 
    return render(request, 'home.html')

def register(request): 
    return render(request, 'register.html')

def login(request): 
    return render(request, 'login.html')


def input(request): 
    return render(request, 'input.html')

def inputform(request):
    inputform = Inputform()   
    inputform.title = request.POST['title']
    inputform.product_name = request.POST['product_name']
    inputform.location = request.POST['location']
    inputform.person_num = request.POST['person_num']
    inputform.price = request.POST['price']
    inputform.link = request.POST['link']
    inputform.account = request.POST['account']
    inputform.date_limit = request.POST['date_limit']
    inputform.explanation = request.POST['explanation']
    inputform.photo = request.POST['photo']
    inputform.save()
    return render(request, 'product/board.html')
    # 폼 제출 후 board.html로 가는 걸로 바꾸기

def detail(request):
    input_information = Inputform.objects
    return render(request, 'detail.html', {'input_information' : input_information})

def board(request):
    inputs = Inputform.objects
    return render(request, 'board.html', {'inputs':inputs})


####################################################################################################

from django.contrib.auth.models import User
from django.contrib import auth


def register(request):
    if request.method == 'POST':     
        if request.POST['password1'] == request.POST["password2"]:        
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home.html')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None: 
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    return render(request, 'login.html')
