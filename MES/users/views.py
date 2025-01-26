from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import CustomUserCreationForm, AuthenticationForm


def start_page_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Личный кабинет
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')  # Перенаправление в личный кабинет
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})  # Окно авторизации


def logout_view(request):
    logout(request)
    return redirect('start_page')  # Перенаправление на гравную страницу


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # авторизуем пользователя после регистрации
            return redirect('dashboard')  # Перенаправление в личный кабинет
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



