from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        # Get the username and password from the form
        email = request.POST['email']
        password = request.POST['password']

        # Use authenticate() to check the credentials
        user = authenticate(request, username=email, password=password)

        # If the credentials are valid, log the user in
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('home')

        # If the credentials are invalid, show an error message
        else:
            messages.error(request, 'Invalid login , Register ?')
    return render(request, 'authorisation/login.html', {})


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email').replace(' ', '').lower()
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if not password_confirmation == password:
            messages.error(request, "Passwords not matching")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
        newUser = User.objects.create_user(
            email=email, username=email, password=password)
        newUser.save()
        auth.login(request, newUser)
        return redirect('home')
    return render(request, 'authorisation/register.html', {})
