from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    context={
        "variable1":"argha is op",
        "variable2":"arghadyati is op"
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")
    
def about(request):
    return render(request,'about.html')
    
def services(request):
    return render(request,'services.html')
    
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "your message has been sent!")

    return render(request,'contact.html')

def handelsignup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        #checks for errors
        if len(username)>10:
            messages.error(request,"username must be under 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,"username must be contain letters and numbers")
            return redirect('home')
        if len(password)<4:
            messages.error(request,"password is too weak")
            return redirect('home')
        
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"Your account has been succesfully created")

    return redirect('home')

def handellogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user=authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successfull")
            return redirect('home')
        else:
            messages.error(request,"Login invalid")
            return redirect('home')
    


def handellogout(request):
    logout(request)
    messages.success(request,"Logged Out")
    return redirect('home')
    
        
        
    

    
