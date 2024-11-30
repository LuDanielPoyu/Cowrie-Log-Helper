from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required = True, 
        widget = forms.EmailInput(attrs = {"class": "register-emailfield"}), 
        help_text = "Please enter a valid email address"
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data["email"].lower()
        if commit:
            user.save()
        return user