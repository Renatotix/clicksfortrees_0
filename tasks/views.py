from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Count
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import UserClick
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
                return redirect('click_view')
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
            return redirect('click_view')



def signout(request):
    logout(request)
    return redirect('signin')


def home(request):
    return render(request, 'home.html')


@login_required
def click_view(request):
    user_click, created = UserClick.objects.get_or_create(user=request.user)  # Obtiene o crea el objeto UserClick

    if request.method == 'POST':
        user_click.add_click()  # Llama al método para agregar un clic
        return render(request, 'clicker.html', {
            'clicks': user_click.clicks,
            'trees_planted': user_click.trees_planted,
            'mensaje': "¡Gracias a ti, plantamos un arbolito!" if user_click.trees_planted > 0 else None
        })

    return render(request, 'clicker.html', {
        'clicks': user_click.clicks,
        'trees_planted': user_click.trees_planted,
        'mensaje': None
    })