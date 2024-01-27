from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        user=request.POST['user']
        print(user)
        s=User(name=name,email=email,password=password,usertype=user)
        s.save()
        return redirect('login')
       
    return render(request,"signup.html")

def login(request):
    if request.method=='POST':
        name1=request.POST['username']
        password1=request.POST['password']
        user=request.POST['user']
        print(user)
        login=User.objects.all().filter(name=name1,password=password1,usertype=user)
        if login:
            if user=="0":
                return render(request,"userlogin.html")
            elif user=="1":
                return render(request,"clientlogin.html")
            else:
                return render(request,"adminlogin.html")
        else:
            messages.error(request, "You are not regsitered or check your credentials" )
            return redirect('login')
    
    return render(request,"login.html")
