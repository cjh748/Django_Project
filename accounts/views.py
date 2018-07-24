from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm, LogInForm


def index(request):
    return render(request, 'html/index.html')


def sign_up(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print("form invalid")
    return render(request, 'html/sign_up.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print("User found!")
            if user.is_active:
                print("Login Successful")
                login(request, user)
                return redirect('menu')
        else:
            print("Invalid login details for User: " + username + ", Pass: " + password)
            return render(request, 'html/login.html')
    else:
        print("Login page started...")
        return render(request, 'html/login.html')
