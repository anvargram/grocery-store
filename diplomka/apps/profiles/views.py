from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, AuthForm


def profiles(request):
    return render(request, 'profiles.html')

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались!")
            return redirect('login.html')
        else:
            messages.error(request, "Вы что то напутали.")
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)

def user_login(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Вы успешно вошли в систему")
                return redirect('index')
            else:
                messages.error(request, "Неверные имя пользователя или пароль.")
    else:
        form = AuthForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, "Вы вышли из системы.")
    return redirect('index')

