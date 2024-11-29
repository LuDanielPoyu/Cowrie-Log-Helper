from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.core.cache import cache
from django.core.mail import EmailMessage
from .forms import CustomUserCreationForm
import random

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if "send" in request.POST:
            email = request.POST.get('email').lower()
            code = generate_verification_code()
            cache.set(email, code, 300)
            
            try:
                send_verification_email(email, code)
                # form.add_error("verification_code", "Verification code has been sent to your email.")
                # 用 render(request, "users/verify.html", {"first_time": True})
            except Exception:
                form.add_error("verification_code", "Please enter a valid email.")
                # 有任何 error 都用 render(request, "users/verify.html", {"error": "錯誤訊息"})
                
            return render(request, 'users/register.html', {"form": form})
                 
        if "verify" in request.POST:
            email = request.POST.get('email').lower()
            if cache.get(email) == request.POST.get('verification_code'):
                cache.set("verification", True)
                form.add_error("verification_code", "Verification successful! You can now register.")  ## NEED FIX ##
                # 改成 alert("Verification success, welcome to Loglytics!");

            ## 需要判斷是否包含非數字的字符嗎? ##
            else:
                form.add_error("verification_code", "Invalid verification code! Please try again.")
        
            return render(request, 'users/register.html', {"form": form})

        if form.is_valid():
            if not cache.get("verification"):
                form.add_error("verification_code", "Please complete the email verification first.")
            email = form.cleaned_data.get("email").lower()

            if User.objects.filter(email__iexact = email).exists():
                form.add_error("email", "This email is already registered! Please use another one.")
            else:
                cache.clear()
                login(request, form.save(), backend = 'django.contrib.auth.backends.ModelBackend') 
                return redirect('homepage_view')
            
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {"form": form})
    

def generate_verification_code():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])


def send_verification_email(email, code):
    email = EmailMessage(
        'Loglytics Registration Verification Code',
        f'Welcome to Loglytics\nYour verification code is: {code}',
        settings.EMAIL_HOST_USER,
        [email],
    )
    
    email.fail_silently = False
    email.send()


def verify_view(request):
    ## Implement verification here ##
    return render(request, "users/verify.html")


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