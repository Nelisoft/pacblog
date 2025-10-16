
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse


# Create your views here.

def RegisterView(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        
        user_data_has_error =False
        
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, 'Username already exists')
            
              
        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, 'Email already exists')
        if password != password1:
            user_data_has_error = True  
            messages.error(request, 'Password doe not match')
            
        if not user_data_has_error:
            new_user =User.objects.create_user(
                first_name =first_name,
                last_name= last_name,
                email=email,
                username=username,
                password=password,
               
            )
            messages.success(request, 'Account created. Login now')
            return redirect('login')
        else:
            return redirect('register')
        
    return render(request, 'userauth/register.html')


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
        
    return render(request, "userauth/login.html")


def LogoutView(request):
   logout(request)
   return redirect('login')

@login_required
def Profile(request):
    return render(request, 'userauth/profile.html')