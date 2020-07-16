from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

def signup(request):
    form = Signup(request.POST)
    if request.method == 'POST' and form.is_valid():
        password = request.POST.get('password')
        alternate_password = request.POST.get('alternate_password')
        if password == alternate_password and password is not None:
            status = form.save()
            return redirect('login:user_login')
        else :
            messages.error(request,'password doesnot match')
            form = Signup(request.POST)
    else :
        form = Signup(request.POST)
    return render(request,'signup/new_user.html',{'form':form})
# Create your views here.
