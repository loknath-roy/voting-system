
from django.contrib import admin
from django.urls import path
from signup.views import Registration
from login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',About,name='about'),
    path('home/',Home,name='home'),
    path('signup/',Registration,name='signup'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('vote/',Vote,name='vote'),
    path('result/',Result,name='result'),
]
