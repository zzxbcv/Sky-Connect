from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


def signup_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm = request.POST["confirm_password"]

        if password == confirm:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect('/login/')

    return render(request, "signup.html")