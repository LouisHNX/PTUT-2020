from django.shortcuts import render, redirect
from .models import team, pool, phase, tournament
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
import random

# Create your views here.
from .models import *
from.forms import CreationUserFormulaire, TournamentForm


def index(request):
    return render(request,'TournoiSport/index.html' )

def registerPage(request):
    form = CreationUserFormulaire()
    if request.method == 'POST':
        form=CreationUserFormulaire(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Compte créé pour '+ user)
            return redirect('login')

    context={'form':form}
    return render(request, 'TournoiSport/register.html',context )

def loginPage(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Le nom d utilisateur ou le mot de passe est incorrect')

    context ={}
    return render(request,'TournoiSport/login.html',context)

def logoutUser(request):
    logout(request)
    return(redirect('login'))

def listteam(request, name):
    name = team.objects.get(name = name)
    data = {'team' : name}
    return render(request, 'TournoiSport/team.html', data) 

def gestionTournoi(request):
    name = team.objects.all()
    data = {'teams' : name}
    return render(request, 'TournoiSport/gestionTournoi.html',data)

def pagecreatetournoi(request):
    return render(request, 'TournoiSport/createTournoi.html')

def createtournoi(request):
    name = request.POST.get('tournamenentName')
    sport = request.POST.get('tournamentSport')
    nb = request.POST.get('tournamentNb')
    place = request.POST.get('tournamentPlace')
    date = request.POST.get('tournamentDate')
    tournament.objects.create(name = name, sport = sport, nb = nb, place = place, date = date)
    html = "<h1>Tournoi Crée {name}{sport}{nb}{place}{date}</h1>"
    
    return HttpResponse(html)

def listetournois(request):    
    return render(request, 'TournoiSport/listeTournois.html')   


def createPool(request):
    id = 1
    nbTeamQualified = 6
    pool_3_4 = False
    teamlist = list(range(1,nbTeamQualified))
    random.shuffle(teamlist)

    if(phase.objects.get(idPhase=1) == 1):
        if(nbTeamQualified % 4) == 0:
            p = phase(nbTeamPerPool = 4)
            p.save()
            nbTeamPerPool = 4
            pool_3_4 = True

        if (nbTeamQualified % 3) == 0:
            p = phase(nbTeamPerPool = 3)
            p.save()
            nbTeamPerPool = 3
            pool_3_4 = True
            
        if pool_3_4 == True:    
            for i in nbTeamQualified:
                pool.objects.create(idPool = id)
                for j in nbTeamPerPool:
                    x = teamlist[j]
                    t = team.objects.get(idTeam=x)
                    t = t.objects.create(idPoolT = id)
                    t.save()
            id += 1


        else: 
            nbTeamPerPool = 4
            while nbTeamQualified - 4 >= 4:
                for i in 4:
                    pool.objects.create(idPool = id)
                    for j in nbTeamPerPool:
                        x = teamlist[j]
                        t = team.objects.get(idTeam=x)
                        t = t.objects.create(idPoolT = id)
                        t.save()
                id += 1
            nbTeamQualified -= 4

            while nbTeamQualified > 0:
                for i in 4:
                    pool.create(pool,id)
                    for j in nbTeamPerPool:
                        x = teamlist[j]
                        t = team.objects.get(idTeam=x)
                        t = t.objects.create(idPoolT = id)
                        t.save()
                id += 1



        name = pool.objects.all()
        data = {'pools' : name}        
        return render(request, 'TournoiSport/gestionTournoi.html', data) 


    else:
        html = "<h1>zebi</h1>"
        return HttpResponse(html)
