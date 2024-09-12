# # Create your views here.
# def register_view(request):
#     form = UserCreationForm()
#     return render(request, 'users/register.html', {"form":form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save()) #register same time as logging in
            return redirect('homepage_view')  # 重定向到主页或其他页面
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})

def login_view(request):
    return render(request, 'users/login.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage_view')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form })