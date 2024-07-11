"""
URL configuration for RideReady project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from RideReady_app import views
from django.core.mail import send_mail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('vehicle/',views.vehicle, name='vehicle'),
    path('tvs/',views.tvs, name='tvs'),
    path('yamaha/',views.yamaha, name='yamaha'),
    path('bajaj/',views.bajaj, name='bajaj'),
    path('emailotp/',views.emailotp,name='emailotp'),
    path('emailotp/data1',views.data1),
    path('emailotp/otp1',views.otp1),
    path('emailotp/customer',views.customer),
    # path('emailotp/kyc',views.kyc),
    # path('emailotp/invoice',views.invoice),
    path('about1/',views.about1, name='about1'),
    
]
