from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def loginpage(request):
    return render(request,'login.html')

def adminhome(request):
    return render(request,'admin/adminhome.html')

def login(request):
    if request.method == "POST":
        un = request.POST.get('u_name')
        ps = request.POST.get('pass')
        user = auth.authenticate(username = un,password = ps)

        if user is not None:
            auth.login(request,user)

            if request.user.is_superuser == 1:
                return redirect('admin_home')
            else:
                return redirect('home')
        else:
            messages.error(request,'User not found')
            return redirect('login_page')
    else:
        return redirect('login_page')
    
def addagencypage(request):
    return render(request,'admin/addagency.html')