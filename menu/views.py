from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def menu(request):
    return render(request, 'html/menu.html')


def logoff(request):
    logout(request)
    return redirect('login')
