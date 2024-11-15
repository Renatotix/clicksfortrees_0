from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('clicker')
            except IntegrityError:
                return render(request, 'register.html', {"form": UserCreationForm, "error": "Username already exists."})
        else:
            form = UserCreationForm()
            return render(request, 'register.html', {"form": form, "error":"Password do not match"})


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'El usuario o la contraseña son incorrectos'})
        else:
            login(request, user)
            return redirect('clicker')


def signout(request):
    logout(request)
    return redirect('signin')


def home(request):
    return render(request, 'home.html')


def clicker(request):
    return render(request, 'clicker.html')