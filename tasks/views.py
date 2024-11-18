from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Count
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import UserClick
from .models import Skin, Perfil , Compra
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signout(request):
    logout(request)
    return redirect('signin')

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




@login_required
def click(request):
    user_click, created = UserClick.objects.get_or_create(user=request.user)  
    if request.method == 'POST':
        user_click.add_click()  
        return render(request, 'clicker.html', {
            'clicks': user_click.clicks,
            'trees_planted': user_click.trees_planted,
        })

    return render(request, 'clicker.html', {
        'clicks': user_click.clicks,
        'trees_planted': user_click.trees_planted,
        'mensaje': None
    })

@login_required
def store(request):
    skins = Skin.objects.all()
    perfil = UserClick.objects.get(user=request.user)

    if request.method == "POST":
        skin_id = request.POST.get("skin_id")
        skin = Skin.objects.get(id=skin_id)

        if perfil.arboles_plantados >= skin.costo_en_arboles:
            perfil.arboles_plantados -= skin.costo_en_arboles
            perfil.save()

            
            compra = Compra(usuario=request.user, skin=skin)
            compra.save()

            
            return redirect('tienda')

        else:
            return render(request, 'tienda.html', {'skins': skins, 'error': "No tienes suficientes árboles."})

    return render(request, 'tienda.html', {'skins': skins})

def ranking(request):
    top_users = UserClick.objects.all().order_by('-trees_planted')[:5]
    
    return render(request, 'ranking.html', {'top_users': top_users})
