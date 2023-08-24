from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        password = request.POST['pass']
        re_password = request.POST['pass2']
        if password == re_password and password != "":
            if User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists():
                 return render(request, 'register.html',{'error':"User already exist or Invalid Credential"})
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=fname,last_name=lname)
                user.save()
                messages.success(request, ('User created successfully'))
                return redirect(logining)
        else:
            return render(request, 'register.html',{'error':"Invalid credential!"})
    else:
        return render (request, 'register.html')

def logining(request):
    if request.user.is_authenticated:
        return redirect (home)
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, ("Loginned Succesfully"))
                return redirect (home)
            else:
                return render(request, 'login.html',{'error':'Invalid Credential!'})
        return render (request, 'login.html')
        
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect (logining)
    
def logouting(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect (logining)                                 
