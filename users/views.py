from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# New registration form created from scratch
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Le compte a été crée {username}!  \n'
                                      f'Tu peux te connecter maintenant :)')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request) :
    return render(request,'users/profile.html')


""" Old registration form (created with django form)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Le compte a été crée {username}!  \n'
                                      f'Tu peux te connecter maintenant :)')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
"""