from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # check for errorneous input
        if len(username) < 5:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('home')
        if (password1 != password2):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your are signup  successfully")
        return redirect('handleLogin')

    else:
        return HttpResponse("404 - Not found")


def handleLogIn(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successsfully loggind')
            return redirect('home')

        else:
            messages.warning
            (request, 'Invalid Credentials, Please try again')
            return redirect('home')

    return HttpResponse('404- Not found')

    return HttpResponse("login")


def handleLogOut(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')
    return HttpResponse('404- Not found')
