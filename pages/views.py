from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def index(req):
    return render(req, 'index.html')

def signup(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('/')
    else:
        form = RegisterForm()
        
    return render(req, 'registration/signup.html', {'form': form})


@login_required(login_url="/login")
def chat(req):
    return render(req, "chat.html")

def news(req):
    return render(req, "news.html")

def about(req):
    return render(req, "about.html")