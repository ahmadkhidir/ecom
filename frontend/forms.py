from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            "class": "form-control form-control-lg login-email",
            "placeholder": "username"
        }
    ))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            "class": "form-control form-control-lg login-password",
            "placeholder": "8+ characters required"
        }
    ))

    class Meta:
        model = User
        fields = ["username", "password"]
