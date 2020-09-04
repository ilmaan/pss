from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')    


def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        
        email = request.POST['email']
        password = request.POST['password1']
        passwordr = request.POST['passwordr']

        if password==passwordr:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')

            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'Password doesnt match')
            return redirect('signup')

        return redirect('/')

    else:
        return render(request,'signup.html')     

        

     

def logout(request):
    auth.logout(request)
    return redirect('/')