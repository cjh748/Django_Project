from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def menu(request):
    return render(request, 'html/menu.html')


# def log_out(request):
#     return render(request, 'html/login.html', {'logout': logout(request)})


def logout_view(request):
    logout(request)
    return redirect('login')
