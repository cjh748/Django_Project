from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def menu(request):
    return render(request, 'menu.html')


def logout_view(request):
    logout(request)
    return redirect('index')
