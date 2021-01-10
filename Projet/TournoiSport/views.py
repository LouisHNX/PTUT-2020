from django.shortcuts import render
from .models import team, pool, phase
import random
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'TournoiSport/index.html' )

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
    name = request.POST.get('tournamenentName','')
    tournament.objects.create(name = name)
    html = "<h1>Tournoi Crée {name}</h1>"
    
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
            while (nbTeamQualified - 4 >= 4):
                for i in 4:
                    pool.objects.create(idPool = id)
                    for j in nbTeamPerPool:
                        x = teamlist[j]
                        t = team.objects.get(idTeam=x)
                        t = t.objects.create(idPoolT = id)
                        t.save()
                id += 1
            nbTeamQualified -= 4

            while (nbTeamQualified > 0):
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


