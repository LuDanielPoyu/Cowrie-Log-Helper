from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email").lower()

            if User.objects.filter(email__iexact = email).exists():
                form.add_error("email", "This email is already registered! Please use another one.")
            else:
                login(request, form.save(), backend = 'django.contrib.auth.backends.ModelBackend') # register same time as logging in
                return redirect('homepage_view')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user(), backend = 'django.contrib.auth.backends.ModelBackend')
            return redirect('homepage_view')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('homepage_view')