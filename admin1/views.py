from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def adminlogin(request):
    if request.user.is_authenticated:
        return redirect(dashboard)
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user  = authenticate(username = username, password = password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect(dashboard)
            else:
                messages.success( request, ("Invalid Credential!"))
                return redirect (adminlogin)
        else:
            return render (request, 'adminlogin.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect(adminlogin)

def users(request):
    if request.user.is_authenticated:
        return render(request, 'user.html')
    else:
        return redirect(adminlogin)

def adduser(request):
    if not request.user.is_authenticated:
        return redirect(adminlogin)
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        re_password = request.POST['pass2']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        if password == re_password and password != "":
            if User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists():
                messages.success(request, ('User already exist or Invalid credentials!'))
                return redirect(users)
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=fname,last_name=lname)
                user.save()
                messages.success(request, ('User created successfully'))
                return redirect(users)
        else:
            messages.success(request, ('Invalid Credential'))
            return redirect(users)
    else:
        return redirect (users)
    
def deleteuser(request):
    if not request.user.is_authenticated:
        return redirect(adminlogin)
    if request.method == 'POST':
        username = request.POST['name']
        if User.objects.filter(username = username).exists():
            user = User.objects.get(username = username)
            user.delete()
            messages.success(request, ('User deleted successfully'))
            return redirect(users)
        else:
            messages.success(request, (f'There is no username called {username}'))
            return redirect (users)
    else:
        return redirect (users)

users_name = ""

def updateuser(request):
    if not request.user.is_authenticated:
        return redirect(adminlogin)
    if request.method =='POST':
        username = request.POST['name']
        user = User.objects.filter(username = username).exists()
        if user :
            global users_name
            users_name = username
            return redirect(updateuser)
        else:
            messages.success(request, ('User does not exist !'))
            return redirect(users)
    return render (request, 'updateuser.html')

def user_update_data(request):
    if not request.user.is_authenticated:
        return redirect(adminlogin)
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        user = User.objects.get(username = users_name)
        user.username = username
        user.email = email
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, ('Updated successfully !'))
        return redirect(users)
    else:
        return render (request, 'updateuser.html')
    
def search_user(request):
    if not request.user.is_authenticated:
        return redirect(adminlogin)
    if request.method =='POST':
        username = request.POST['name']
        user = User.objects.filter(username = username).exists()
        if user :
            values = User.objects.filter(username = username)
            return render (request, 'search.html',{'value':values})
        else:
            messages.success(request, ('User does not Exist!'))
            return redirect(users)   

def search_back(request):
    return redirect(users)

def view_data(request):
    if not request.user.is_authenticated:
        return redirect(adminlogin)
    values = User.objects.order_by('id')
    return render(request, 'view.html',{'value':values})

def logouting(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect (adminlogin)