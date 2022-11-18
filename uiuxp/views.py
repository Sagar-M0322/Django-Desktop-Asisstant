from django.shortcuts import render
import os
import requests


def button(request):
    return render(request, 'landing page.html')


def user(request):
    return render(request, 'user.html')


def novice(request):
    return render(request, 'novice.html')


def inter(request):
    return render(request, 'inter.html')


def expert(request):
    return render(request, 'exper.html')


def click(request):
    # ui.main()
    os.system('python ui.py')
    return render(request, 'landing page.html')
