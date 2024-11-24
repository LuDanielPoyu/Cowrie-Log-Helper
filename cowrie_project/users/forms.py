from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required = True, 
        widget = forms.EmailInput(attrs = {"class": "register-emailfield"}), 
        help_text = "Please enter a valid email address"
    )
    
    verification_code = forms.CharField(
        required= False,
        widget = forms.TextInput(attrs = {"class": "register-verifyfield"}),
        label = "Verification Code",
        help_text = "Please enter verification code"
    )

    class Meta:
        model = User
        fields = ("username", "email", "verification_code", "password1", "password2")

    def save(self, commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data["email"].lower()
        if commit:
            user.save()
        return user