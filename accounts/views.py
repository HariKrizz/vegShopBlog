
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method == 'POST':
        user_name = request.POST["username"]
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        email = request.POST["email"]
        passwd1 = request.POST["password1"]
        passwd2 = request.POST["password2"]
        
        if passwd1 == passwd2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username Exists!")
                return redirect('register')         
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Username Exists!")
                return redirect('register')        
            else:               
                user = User.objects.create_user(username=user_name,password=passwd1,email=email,first_name=fname,last_name=lname)
                user.save() 
                print("User Registered")
                return redirect('login')
        else:
            print("Password does not match!")
            return redirect('/')
    else:
        return render(request,'registration.html')

def login(request):
    if request.method == 'POST':
        user = request.POST['Username']
        passwd1 = request.POST['Password']
        user = auth.authenticate(username=user,password=passwd1)

        if user is not None:
            auth.login(request,user)               
            print("Login Successful")
            return redirect('/')
        else:
            messages.info(request,"Invalid Username or Password")    
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
        