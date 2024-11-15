from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Count
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Planting, Reward, TreeType
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

@login_required
def click_plant(request):
    tree_type = TreeType.objects.first() 

    # Registra la plantación
    Planting.objects.create(user=request.user, tree_type=tree_type)

    # Verifica y otorga recompensas
    user_plantings = Planting.objects.filter(user=request.user).count()
    unlocked_rewards = Reward.objects.filter(required_plantings__lte=user_plantings, tree_type=tree_type)
    for reward in unlocked_rewards:
        reward.unlocked_by.add(request.user)
    
    return redirect("clicker")

@login_required
def leaderboard(request):
    leaderboard = User.objects.annotate(total_plantings=Count('planting')).order_by('-total_plantings')
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard})

@login_required
def rewards(request):
    rewards = Reward.objects.filter(unlocked_by=request.user)
    return render(request, 'rewards.html', {'rewards': rewards})

def signout(request):
    logout(request)
    return redirect('signin')


def home(request):
    return render(request, 'home.html')


def clicker(request):
    return render(request, 'clicker.html')