from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# create account관련된 UserCreatinForm 상속받아서
# 사용자지정 form class UserForm 생성
class UserForm(UserCreationForm):
    # 사용자 지정 form(학번, 이메일, 증명 이미지)을 통해
    # 우리가 원하는 form을 받을 수 있게 미리 정의함
    stdnumber = forms.Field(label="학번")
    email = forms.EmailField(label="이메일")
    veriImg = forms.ImageField(label="증명사진")

    class Meta:
        model = User
        fields = ("stdnumber", "username", "veriImg", "password1", "password2", "email")
