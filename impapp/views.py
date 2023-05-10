from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect





def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            return redirect('login')
    return render(request,"login.html")


def register(request):
        if request.method=='POST':
            print('post data : ',request.POST)
            username=request.POST['user_name']
            first_name = request.POST['fst_name']
            last_name = request.POST['end_name']
            email = request.POST['Email']
            password= request.POST['Password']
            c_password=request.POST['cnfrm_password']
            if password==c_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username taken")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"username taken")
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request,"password not matching")
                return redirect('register')
            return redirect('/')
        return render(request,"register.html")






def logout(request):
    auth.logout(request)
    return redirect('/')
