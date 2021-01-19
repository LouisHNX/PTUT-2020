from django.shortcuts import render, redirect
from .models import team, pool, phase
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
import random

# Create your views here.
from .models import *
from.forms import CreationUserFormulaire


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
    if request.method == 'POST':
        tname = request.POST.get('tournamenentName','')
        #tournament.objects.create(name = tname)
        messages.success(request,'Tournoi crée '+ tname)
        return redirect('pagecreatetournoi')

    return render(request, 'TournoiSport/createTournoi.html')


def listetournois(request):    
    return render(request, 'TournoiSport/listeTournois.html')   


def createPool(request):
    Phase = phase.objects.get(idPhase = 1)
    nbTeamQualified = Phase.nbTeamQualified
    pool_3_4 = False
    teamlist = list(range(1,nbTeamQualified+1))
    random.shuffle(teamlist)
    idListe = 0  
    i = 0
    j = 0

    if(Phase.idPhase == 1):

        if(nbTeamQualified % 4) == 0:
            Phase.nbTeamPerPool = 4
            Phase.save()
            nbTeamPerPool = 4
            nbPool = nbTeamQualified // 4
            pool_3_4 = True
            

        if (nbTeamQualified % 3) == 0:
            Phase.nbTeamPerPool = 3
            Phase.save()
            nbTeamPerPool = 3
            nbPool = nbTeamQualified // 3
            pool_3_4 = True


        if pool_3_4 == True:  
            id = 1
            
            for i in range(nbPool):
                Pool = pool(idPool = id)
                Pool.save()
                for j in range(nbTeamPerPool):
                    x = teamlist[idListe]
                    t = team.objects.get(idTeam=x)
                    t.idPoolT = id
                    t.save()
                    idListe +=  1

                id += 1

        
        else:
            id = 1 
            nbTeamPerPool = 4
            while nbTeamQualified >= 4:
                Pool = pool(idPool = id)
                Pool.save()
                for j in range(nbTeamPerPool):
                    x = teamlist[idListe]
                    t = team.objects.get(idTeam=x)
                    t.idPoolT = id
                    t.save()
                    idListe += 1

                nbTeamQualified -= 4
                id += 1
                                 

            nbTeamPerPool = 3
            while nbTeamQualified > 0:
                Pool = pool(idPool = id)
                Pool.save()

                for j in range(nbTeamPerPool):
                    x = teamlist[idListe]
                    t = team.objects.get(idTeam=x)
                    t.idPoolT = id
                    t.save()   
                    idListe += 1

                nbTeamQualified -= 3
                id += 1

             
            

        #name = pool.objects.all()
        #data = {'pools' : name}        
        #return render(request, 'TournoiSport/gestionTournoi.html', data) 
        html = "<h1>OUIIIIIIIII</h1>"
        return HttpResponse(html)


    else:
        html = "<h1>zebi</h1>"
        return HttpResponse(html)
