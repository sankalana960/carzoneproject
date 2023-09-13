from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contact.models import Contact
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now loged in.')
            return redirect('dashboard')
        else:
            return redirect('login')  

    return render(request, 'account/login.html')






def register(request):

    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
                if User.objects.filter(username=user_name).exists():
                    messages.error(request,'username already exists')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'email already exists')
                        return redirect('register')
                    else:
                        user = User.objects.create_user(first_name=first_name, last_name=last_name,email=email, username=user_name, password=password)
                        auth.login(request, user)
                        return redirect('dashboard')
        else:
            messages.error(request, "password doesn't match")
            return redirect('register')

    return render(request, 'account/register.html')


def dashboard(request):
    user_inquiry = Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
    data = {
        'user_inquiry':user_inquiry
    }
    return render(request, 'account/dashboard.html',
                  data)


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')