from django.urls import path

from . import views


app_name = 'sw'


urlpatterns = [
    # 메인페이지
    path('', views.home, name='home'),
    # 학생회 소개
    path('swintro/', views.introduce, name='swintro'),
    # 학생회 연혁
    path('swhistory/', views.history, name='swhistory'),
]
