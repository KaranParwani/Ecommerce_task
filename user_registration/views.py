from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/") 
        else:
            messages.info(request, message = 'INVALID CREDENTAILS')
            return redirect('login')
    
    else:
        return render(request, "login.html")
    
def logout(request):
    auth.logout(request) 
    return redirect('/')

def home(request):
    return  render(request, "home.html")

def testing(request):
    return render(request, "testing.html")

def registration(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1==password2:    
            if User.objects.filter(username=username).exists():
                # print('Username Taken')
                messages.error(request, message = 'Username Exists')
                return redirect('registration')
                                                                         
            elif User.objects.filter(email=email).exists():
                # print('email Taken')    
                # messages.info(request,'Email Already Taken')
                messages.error(request, message = 'Email Already Exists')
                return redirect('registration')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,password=password1, email=email)
                user.save();
                # print('User created')
                # messages.info(request,'SUCCESS')
                # messages.info(request, message = 'SUCCESS')
                print('success')
                return redirect('login')                                                         
        else:
            messages.info(request, message = 'Password not Matching')
            return redirect('registration')
        return redirect('login')
    
    else:
        return render(request, 'registration.html')    


