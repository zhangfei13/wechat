"""managePlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ferry_management_platform import views

urlpatterns = [
    path('', views.wechat_home, name='wechat_home'),
    path('admin/', admin.site.urls),
    path('admin2/',  views.admin2, name='admin2'),
    path('jilu/', views.jilu, name='jilu'),
    path('certification/', views.certification, name='certification'),
    path('certification_inputinfo/', views.certification_inputinfo, name='certification_inputinfo'),
    path('v_user/', views.v_user, name='v_user'),
    path('huimin_service/', views.huimin_service, name='huimin_service'),
    path('information_search/', views.information_search, name='information_search'),
    path('jiaoguan12123/', views.jiaoguan12123, name='jiaoguan12123'),
    path('woshihaosiji/', views.woshihaosiji, name='woshihaosiji'),
    path('self_proc_illegal_notice/', views.self_proc_illegal_notice, name='self_proc_illegal_notice'),
]
