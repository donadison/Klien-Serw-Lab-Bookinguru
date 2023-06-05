"""
URL configuration for bookingooroo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import check_booking, home, hotel_detail, register, login1

urlpatterns = [
    path('check_booking/', check_booking, name='check_booking'),
    path('home/', home, name='home'),
    path('hotel-detail/<int:uid>/', hotel_detail, name='hotel_detail'),
    path('register/', register, name='register'),
    path('login1/', login1, name='login1'),
]
