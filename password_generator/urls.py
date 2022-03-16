"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
from generator import views
from django.urls import path

urlpatterns = [
    # path('adal/', admin.site.urls),
    path('', views.home),
    path('page1/', views.page1),
    path('page1/page1.1', views.page1),
    path('page2/', views.page2),
    path('page3/', views.page3),
    path('page4/', views.page4),
]
