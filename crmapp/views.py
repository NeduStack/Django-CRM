from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate( request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been Logged in Successfully!")
            return redirect('index')
        else:
            messages.success(request, "Username or Password Not Correct!")
            return redirect('index')
    else:
        return render(request, 'index.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully Logged out!")
    return redirect('index')

def register(request):
    return render(request, 'register.html', {})
