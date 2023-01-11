from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'landing/index.html', {})


def about(request):
    return render(request, 'landing/about.html', {})


def about(request):
    return render(request, 'landing/about.html', {})


def services(request):
    return render(request, 'landing/services.html', {})


def login(request):
    return render(request, 'authorisation/login.html', {})


@login_required
def blog(request):
    return render(request, 'first_func/first_func.html', {})


@login_required
def content(request):
    return render(request, 'second_func/second_func.html', {})


@login_required
def emails(request):
    return render(request, 'third_func/third_func.html', {})
# blog first fun , content second func ,other one third
