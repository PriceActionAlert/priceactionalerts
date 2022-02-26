from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .userform import CustomRegisterForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from .models import *
from .emailactivation import *
import uuid

import pandas as pd
#import numpy as np
import yfinance as yf
from datetime import datetime, date, timedelta
import sys
import datetime, calendar
from collections import OrderedDict
from pytz import timezone
import time
import math

# Create your views here.


def register(request):

    if request.method=='POST':
        register_form = CustomRegisterForm(request.POST)
        username = request.POST['username']
        useremail = request.POST['email']
        userpassword = request.POST['password1']
        ind_time = datetime.datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
        if register_form.is_valid():
            user = User.objects.create_user(username=username,email=useremail)
            user.set_password(userpassword)
            user.is_active=False
            user.save()
            email_token = str(uuid.uuid4())
            profile = Profile.objects.create(
                user=user,
                email_token=email_token,
                nudgedata={'nudgenotification':False,'maxloss': '', 'maxprofit': '', 'nudgeStockList': ['', '', '', '', '', '', '', '', '', ''],'nudgeStockListPrice': ['', '', '', '', '', '', '', '', '', '']},
            )
            #print("Register Profile:",profile)
            send_email_token(useremail,profile.email_token)
            messages.success(request, "New Account Created. Check For Account Activation Email.")
            return redirect("users:login")

    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html',{'register_form': register_form})

def verify(request,token):
    try:
        profile_obj = Profile.objects.get(email_token = token)
        username = profile_obj.user
        user_obj = User.objects.get(username=username)
        user_obj.is_active=True
        user_obj.save()
        profile_obj.save()

        return redirect("users:login")

    except Exception as e:
        return HttpResponse("Invalid Token. Activation Failed.")

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        #print("User: {} and {}. User: {}".format(username, password, user))
        if user is not None:
            login(request, user)
            profile_obj = Profile.objects.get(user = user)
            profile_stocks = profile_obj.stocks
            profile_notification = profile_obj.notification
            #print("Login User: {} and {}".format(profile_stocks,profile_notification))
            return redirect('dailycandle:index')
        else:
            messages.success(request, "Incorrect Username or Password")
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out !!!")
    return render(request, 'login.html')



