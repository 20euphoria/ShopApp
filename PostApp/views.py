from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import *

@login_required(login_url="login")
def home(request):
    batch_obj = Post.objects.filter(user=request.user)
    context = {"post": batch_obj}
    return render(request, "home.html", context)


@login_required(login_url="login")
def create_post(request):
    if request.method == "POST":
        text = request.POST["ftext"]
        if len(text) == 0:
            messages.error(request, "Enter Some Intersting Data")
            return redirect("home")
        else:
            pp = Post(user=request.user,text=text, created_at=datetime.now(), updated_at=datetime.now())
            pp.save()
            messages.success(request, 'Post created successfully')
            return redirect("home")
    else:
        messages.error(request, 'Something went wrong')
        return redirect("home")


@login_required(login_url="login")
def delete_post(request, id):
    if request.method == "GET":
        post_obj = Post.objects.get(id=id)
        post_obj.delete()
        return redirect("home")


@login_required(login_url="login")
def post_detail(request, id):
    if request.method == "GET":
        post_obj = Post.objects.filter(id=id,user=request.user)
        context = {"data":post_obj}
        return render(request, "details.html", context)


def loginuser(request):
    if request.method == "POST":
        uname = request.POST["username"]
        pwd = request.POST["password"]
        user_auth = authenticate(username=uname, password=pwd)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('home')
        else:
            messages.error(
                request, 'Entered username or password is incorrect')
    return render(request, "login.html")


def logoutuser(request):
    logout(request)
    return redirect('login')


def signupuser(request):
    if request.method == "POST":
        uname = request.POST.get("id_username")
        pass1 = request.POST.get("id_password1")
        pass2 = request.POST.get("id_password2")
        if User.objects.filter(username__iexact=uname).exists():
            messages.error(
                request, "This  Username is  already exist please try another email")
            return redirect('signup')
        else:
            if pass1 == pass2:
                User.objects.create_user(
                    username=uname, password=pass1)
                messages.success(
                    request, 'Congratulations you have registered successfully')
                return redirect('login')
            else:
                messages.error(
                    request, "The password confirmation does not match with password.")
                return redirect('signup')
    return render(request, "signup.html")
