"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
path('home/',views.home_view),
    path('login_conf/',views.suc_conf),
    path('forgot/',views.forgot_view),
    path('forgot2/',views.forgot2_view),
    path('class_select/',views.class_select_view),
    path('class_select2/',views.class_select2_view),
    path('final_list/',views.list_view),
    path('room_view/',views.room_view),
      url(r'^$',views.home_view)
]
