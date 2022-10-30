from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User  #for user model, django built-in
from django.contrib import auth, messages
from django.contrib.auth import authenticate
import math

from .models import Profile,TodoList

# Create your views here.


def index(request):
    username = request.user
    print(username)
    return render(request, 'index.html' , {'username': username})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2'] #confirmation password
        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already there")
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username = username, password = password)
                user.save()
                user_login = auth.authenticate(username = username, password = password)
                auth.login(request, user_login)
            
                user_model = User.objects.get(username = username)
                new_profile = Profile.objects.create(user = user_model)
                new_profile.save()

                return redirect("signin")
        else:
            messages.info(request, "Both the passwords are different")
            return render(request, "signup.html")
            
    else:
        return render(request, "signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username , password = password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'No account present')
            return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('signin')

def profile(request, pk):
    user_object = User.objects.get(username = pk)
    user_profile = Profile.objects.get(user = user_object) #user_profile has the things related to that user
    todolist = TodoList.objects.filter(username = pk).order_by('-average')

    context = {
        'user_object' : user_object,
        'user_profile' : user_profile,
        'todolist' : todolist,
    }
    return render(request, 'profile.html', context)

def upload(request):
    print('check1')
    if request.method == 'POST':
        user = request.user.username
        print(user)
        title = request.POST['title']
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
        average = (int(num1)+ int(num2)+ int(num3))//3
        print(average)

        if TodoList.objects.filter(username = user, title=title).exists():
            update_todo = TodoList.objects.filter( title = title).update(num1 = num1, num2= num2, num3= num3,average= average)
        else:
            new_todo  = TodoList.objects.create(username = user, title = title, num1 = num1, num2 = num2, num3 = num3, average=average)
            new_todo.save()

        return redirect('profile/' + user)
    else:
        return redirect('/profile')

def delete(request):
    print('check1')
    if request.method == 'POST':
        user = request.user.username
        print(user)
        title = request.POST['title']
        
        del_todo  = TodoList.objects.filter(username = user, title = title)
        
        if del_todo:
            del_todo.delete()
        else:
            return redirect('profile/' + user)
        return redirect('profile/' + user)
    
    else:
        print('check2')
        return redirect('/' )
