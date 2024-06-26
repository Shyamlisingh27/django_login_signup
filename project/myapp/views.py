
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm

# views hi saare html files ko handle krta h
#django framework h jism python code likhte hain

#HTTP Request Methods: HTTP supports several request methods, the most common ones being GET and POST.
#GET requests are typically used to retrieve data from the server.
#POST requests are used to submit data to be processed by the server (e.g., submitting a form).

#2 global variable email aur password bnayenge usi m store krenge emails aur passwords 
#agr post ho gya h mtlb submit ho gya to saara kch emails ya passwords dictionary k form m hota h h browse krr k pta krna h ki email h ya password h to alg variable m store krenge unko 

#agr form submit krr denge to method post k saath form submit hoga kyuki login.html m <form actn... method="POST"> likhe the
#then nxt querry backend m jayega
#then in backend is particular login.html file ko views.py is handeling kyuki dono myapp folder ka h
#to form submit hua to saath m usme jo bhi tha email aur password wo dictionary k form m backend(means views.py) m submit hua h

#python m dictionary key-value pair hota h double quotes k andar key...key is unique... d={"email":"shyamlisingh14@gmail.com" ,"password":"123"}  but password hashform m store hota h strng form m ni

def login_action(request):
    #global email,password
    if request.method=="POST":
        
#the moment user presses submit button method turns to post
#1st get the entire form bcs we have to link it with database
        form=LoginForm(request.POST)
        
        if form.is_valid():
            #form.save()            #saves data in database
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('welcome')
            else:
                return redirect('error')
        else:
            return HttpResponse("Failed to save data!")
    else:   #method=="GET"                       #if user has not submitted
        form=LoginForm()
    return render(request,'myapp/login.html',{'form':form})

def logout_action(request):
    logout(request)
    return redirect('login')

def welcome(request):
    return render(request,'myapp/welcome.html')

def error(request):
    return render(request,'myapp/error.html')
