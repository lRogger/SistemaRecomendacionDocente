from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from authentication.forms import SignUpForm


# Vista para crear una cuenta de usuario
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Log in the new user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('signin')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'sign-up.html', context)


# Vista para iniciar sesión
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_name'] = user.username
            return redirect('/modules/')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('signin')
    else:
        return render(request, 'sign-in.html', {})


def logout_user(request):
    logout(request)
    return redirect('signin')


def home(request):
    return render(request, 'home.html', {})
