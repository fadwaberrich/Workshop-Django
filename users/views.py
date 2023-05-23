from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login
# Create your views here.

def login_view (request):
    form = LoginForm
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Event_ListEvent_V')
    return render(request,'users/login.html',{'form':form})

def register(request):
    form = UserRegistrationForm()

    if request.method =='POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Event_ListEvent_V')
    
    return render(request,'users/login.html',{'form':form})

