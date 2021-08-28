from django import http
from django.shortcuts import render, redirect, HttpResponse
from .models import Users
from django.contrib import messages
import bcrypt

def register(request):

  if request.method == 'GET':
    return render(request,'register.html')

  else:
    name=request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    password_confirm = request.POST['password_confirm']

    errors=Users.objects.basic_validator(request.POST)
    if len(errors) > 0:

      for key,errormsg in errors.items():
        messages.error(request, errormsg)

    # if password != password_confirm:
    #   messages.error('Las contraseñas no coinciden. Vuelva a intentarlo')
      return redirect('/register')
    
    user = Users.objects.create(name=name, email=email, password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())

    request.session['user'] = {
      'id':user.id,
      'name': user.name,
      'email': user.email,
      'avatar':user.avatar
    }

    return redirect('/register/mainpage')

def mainpage(request):
  return render(request, 'mainpage.html')

def login(request):

    email = request.POST['email']
    password = request.POST['password']
    
    try:
      user = Users.objects.get(email=email)
    except Users.DoesNotExist:
      messages.error(request, 'Usuario y/o contraseña inválidos')
      return redirect('/register')

    if not bcrypt.checkpw(password.encode(), user.password.encode()):
      messages.error(request, 'Usuario y/o contraseña inválidos')
      return redirect('/register')
    
    request.session['user'] = {
    'id':user.id,
    'name': user.name,
    'email': user.email,
    'avatar':user.avatar
    }
    messages.success(request, f'Hola {user.name}')
    return redirect('/register/mainpage')

def logout(request):
  request.session['user'] = None
  return redirect('/register')