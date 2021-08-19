from django import http
from django.shortcuts import render, redirect, HttpResponse
from .models import Shows, Networks

def redir(request):
  return redirect('/shows')

def index(request):
  context = {
      'shows' : Shows.objects.all(),
      'networks': Networks.objects.all(),
  }
  return render(request, 'shows.html', context)

def newshow(request):
  context = {
    'shows' : Shows.objects.all(),
    'networks': Networks.objects.all(),
  }
  return render(request, 'new.html', context)

def create(request):


  tit = request.POST["tit"]
  des = request.POST["des"]
  reldate = request.POST["reldate"]

  if request.POST['net'] == 'other':
    netw = Networks.objects.create(name=request.POST['newnetwork'])

  else:
    netw = Networks.objects.get(id=request.POST["net"])

  Shows.objects.create(title=f'{tit}', description=f'{des}', rel_date=f'{reldate}', network=netw)

  return redirect ('/shows')

def info(request, showid):

  context = {
      'show' : Shows.objects.get(id=showid),
      'nets': Networks.objects.all(),
  }
  return render(request, 'show_info.html', context)

def edit(request,showid):
  context = {
      'show' : Shows.objects.get(id=showid),
      'nets': Networks.objects.all(),
  }

  return render(request, 'edit.html', context)

def editshow(request,showid):

  editshow = Shows.objects.get(id=int(showid))

  tit = request.POST["tit"]
  des = request.POST["des"]
  reldate = request.POST["reldate"]
  net = request.POST["net"]

  editshow.title = f'{tit}'
  editshow.description = f'{des}'
  editshow.rel_date = f'{reldate}'
  editshow.network = Networks.objects.get(id=f'{net}')
  editshow.save()

  return redirect ('/shows')

def delete(request, showid):

  delshow = Shows.objects.get(id=showid)
  delshow.delete()

  return redirect('/shows')