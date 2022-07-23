from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import auth
from .models import Charity

# Create your views here.
def home(request):
    if (request.method=='POST') and ('qeydiyyat' in request.POST):
        username=request.POST.get("sign_up_name")
        password=request.POST.get("sign_up_password")
        confirm=request.POST.get("sign_up_confirm")
        if password!=confirm:
            print("sehvlik var")
            return redirect('home')
        new_user=User.objects.create_user(username=username,password=password)
        new_user.save()
        print("Her sey duzdur")
        return redirect('home')
    elif (request.method == 'POST') and ('destek' in request.POST):
        username=request.POST.get("sign_in_name")
        password=request.POST.get("sign_in_password")
        money=request.POST.get("charity")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            new_user=Charity(username=username,password=password,money=money)
            new_user.save()
            return render(request,'yoxlama.html')
    return render(request,'charity.html')


