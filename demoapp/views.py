import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import School
from PyDictionary import PyDictionary


dictionary_initialisation = PyDictionary()

# Create your views here.
def index(request):
    schools = School.objects.all()
    return render(request, 'index.html', {'schools': schools})
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create(username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')

    return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid login details')
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def dictionary(request):

    if request.method == 'POST':
        word = request.POST['word']

        meaning = dictionary_initialisation.meaning(word)['Noun'][0]
        
        return render(request, 'dictionary.html', {'word': word, 'meaning':meaning})
    
    return render(request, 'dictionary.html')