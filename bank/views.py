from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import *

from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'bank/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'bank/register.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            messages.error(request, 'Wrong username/password')
            return HttpResponse("Error")
    return render(request, 'bank/login.html')

