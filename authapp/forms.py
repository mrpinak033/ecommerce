from django import forms
from django.forms import PasswordInput
from .models import SignUp
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        widgets = {'pwd': forms.PasswordInput(),'cpwd': forms.PasswordInput(), }
        fields = ['uname','fname','lname','dob','mobno','email','pwd','cpwd']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())
