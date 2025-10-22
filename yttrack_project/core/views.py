from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quadro
from .forms import QuadroForm

def user_login(request):
    if request.method == 'POST':
        identifier = request.POST.get('email')
        password = request.POST.get('password')

        # tentar autenticar diretamente por username, caso usuário use username
        user = authenticate(request, username=identifier, password=password)
        if user is None:
            # tenta localizar por email e autenticar pelo username
            from django.contrib.auth import get_user_model
            User = get_user_model()
            try:
                u = User.objects.get(email__iexact=identifier)
                user = authenticate(request, username=u.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            return redirect('core:login')  # será alterado para quadros depois
        else:
            messages.error(request, 'E-mail ou senha inválidos.')
    return render(request, 'core/login.html')

def user_logout(request):
    logout(request)
    return redirect('core:login')

@login_required
def quadros(request):
    lista = Quadro.objects.all()
    return render(request, 'core/quadros.html', {'quadros': lista})

@login_required
def novo_quadro(request):
    if request.method == 'POST':
        form = QuadroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:quadros')
    else:
        form = QuadroForm()
    return render(request, 'core/quadro_form.html', {'form': form})