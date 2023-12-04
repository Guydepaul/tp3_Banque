from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Compte

def accueil_view(request):
    return render(request, 'banque/accueil.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Identifiant ou mot de passe incorrect."
            return render(request, 'banque/login.html', {'error_message': error_message})
    else:
        return render(request, 'banque/login.html')


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Créer un nouvel utilisateur avec l'email et le mot de passe
        user = User.objects.create_user(username=email, email=email, password=password)
        # Créer un compte associé à l'utilisateur
        Compte.objects.create(user=user)
        return redirect('/login')
    else:
        return render(request, 'banque/register.html')


def dashboard_view(request):
    if request.user.is_authenticated:
        user = request.user
        compte = Compte.objects.get(user=user)
        return render(request, 'banque/dashboard.html', {'compte': compte})
    else:
        return redirect('login')


def deposer_view(request):
    if request.method == 'POST':
        montant = int(request.POST.get('montant'))
        compte = Compte.objects.get(user=request.user)
        compte.solde += montant
        compte.save()
        return redirect('dashboard')
    else:
        return render(request, 'banque/deposer.html')


def retirer_view(request):
    if request.method == 'POST':
        montant = int(request.POST.get('montant'))
        compte = Compte.objects.get(user=request.user)
        if montant <= compte.solde:
            compte.solde -= montant
            compte.save()
        return redirect('dashboard')
    else:
        return render(request, 'banque/retirer.html')
