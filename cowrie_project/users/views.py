from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.core.cache import cache
from django.core.mail import EmailMessage
from .forms import CustomUserCreationForm
import random


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


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email').lower()

            if User.objects.filter(email__iexact = email).exists():
                form.add_error("email", "This email is already registered! Please use another one.")

            else:
                request.session['username'] = form.cleaned_data['username']
                request.session['password'] = form.cleaned_data['password1']
                request.session['email'] = email
                
                code = generate_verification_code()
                send_verification_email(email, code)
                cache.set(email, code, 300)
                
                return render(request, 'users/verify.html', {"first_time": True})
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {"form": form})


# 有任何 error 都用 render(request, "users/verify.html", {"error": "錯誤訊息"})  
def verify_view(request):
    if request.method == "POST":
        email = request.session['email']
        if not email:
            return redirect('registration_view')            
        
        if "verify" in request.POST:
            if cache.get(email) == request.POST.get('verification_code'):
                try:
                    user = User(
                        username = request.session['username'],
                        email = email
                    )
                    user.set_password(request.session['password'])
                    user.save()
                    cache.clear()
                    
                    login(request, user, backend = 'django.contrib.auth.backends.ModelBackend')
                    return redirect('homepage_view')
                
                except Exception:
                    return render(request, "users/verify.html", {"error": "Something wrong happens. Please try again later."})
            else:
                return render(request, "users/verify.html", {"error": "Invalid verification code! Please try again."})
        
        else:  # resend code
            try:
                code = generate_verification_code()
                send_verification_email(email, code)
                cache.set(email, code, 300)
                
                return render(request, "users/verify.html", {"resend": True})
            
            except Exception:
                return render(request, "users/verify.html", {"error": "Failed to resend verification code. Please try again later."})
        
    return render(request, "users/verify.html")


def generate_verification_code():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])


def send_verification_email(email, code):
    email = EmailMessage(
        'Loglytics Registration Verification Code',
        f'Hello, welcome to Loglytics!\nHere is your verification code: {code}',
        settings.EMAIL_HOST_USER,
        [email],
    )
    
    email.fail_silently = False
    email.send()