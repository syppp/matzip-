from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Inputform, Profile

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
    inputform.photo = request.FILES['photo']
    inputform.save()
    return redirect('board')


####################################################################################################

from django.contrib.auth.models import User
from django.contrib import auth


def register(request):    
    if request.method == 'POST':     
        if request.POST['password1'] == request.POST["password2"]:        
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)  
            profile = Profile()
            profile.user = request.user          
            profile.nickname = request.POST['nickname']
            profile.email = request.POST['email']
            profile.phone_num = request.POST['phone_num']
            profile.school = request.POST['school']
            profile.save()
            return redirect('home')
    return render(request, 'register.html')


def login(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username = username, password = password)
        if user is not None: 
            auth.login(request, user)
            return redirect('home')         
        else:                              
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    return render(request, 'login.html')  

def logout(request):   
    auth.logout(request)         
    return redirect('home')

def mypage(request):     
    user_now = request.user
    a = user_now.id
    mypage = User.objects.get(id=a)
    return render(request, 'mypage.html', {'user': mypage})
    

