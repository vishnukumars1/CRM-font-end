from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home,name='home'),
    path('login_page',views.loginpage,name='login_page'),

    path('admin_home',views.adminhome,name='admin_home'),

    path('login',views.login,name='login'),

    path('add_agency_page',views.addagencypage,name='add_agency_page'),
]