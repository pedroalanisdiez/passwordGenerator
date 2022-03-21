import random
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUXYZ')
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})    

def about(request):
    return render(request, 'generator/about.html')