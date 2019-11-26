from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.middleware import http
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from .models import SignUp
import http.client
import random
import json


def signup(request):
    if request.method == 'POST':
        regform = SignUpForm(request.POST)
        if regform.is_valid():
            x = otp_send(request)
            if x:
                return render(request, 'otp_input.html')
            else:
                return render(request, 'signup.html')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def otpvalidation(request):
    newotp = request.POST["otp"]
    oldotp = request.POST["otp"]
    if newotp == oldotp:
        form = SignUpForm(request.session["details"])
        new_user = User.objects.create_user(username=request.session["uname"], password=request.session["pwd"])
        new_user.save()
        form.save()
        login(request, new_user)
        return render(request, 'auth_home.html')
    else:
        return render(request, 'otp_input.html')

def otp_send(request):
    ot = str(random.randint(100000, 999999))
    mobno = request.POST["mobno"]
    request.session["uname"] = request.POST["uname"]
    request.session["pwd"] = request.POST["pwd"]
    request.session["details"] = request.POST
    request.session["otp"] = ot
    conn = http.client.HTTPConnection("api.msg91.com")
    payload = "{ \"sender\":\"PINAKR\", \"route\": \"4\", \"country\": \"91\", \"sms\": [ { \"message\":\"" + ot + "\",\"to\": [ \"" + mobno + "\" ] } ] }"
    headers = {
        'authkey': "300125AkduUIzE75dada7e5",  # PLEASE ENTER THE AUTHKEY BEFORE EXECUTING THE PROGRAM
        'content-type': "application/json"
    }
    conn.request("POST", "/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encrypt=&message=&flash=&unicode=&schtime=&afterminutes=&response=&campaign=", payload, headers)
    data = conn.getresponse()
    res = json.loads(data.read().decode("utf-8"))
    print(res)
    if res["type"] == "success":
        return True
    else:
        return False


@login_required()
def login(request):
    return render(request, "auth_home.html")


def my_logout(request):
    return render(request, "index.html")