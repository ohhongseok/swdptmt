# 계정관련 app 정의 부분
# 계정 생성 및 로그인과 관련된 request, action을 정의하고 있다.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from account.forms import UserForm
from django.contrib import messages
from django.contrib import auth


# 로그인 및 회원가입 view


def login(request):
    return render(request, 'login.html')


# 회원가입 action

def signup(request):
    if request.method == "POST":
        if request.POST['passworld1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['name'], password=request.POST['password1'],
                                            stdnumber=request.POST['stdnumber'], email=request.POST['email'],
                                            veriImg=request.POST['veriImg'])
            auth.login(request, user)
            return redirect('/')
    return render(request, 'register.html')

