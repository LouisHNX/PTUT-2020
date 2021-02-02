from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('gestionTournoi/', views.gestionTournoi, name="gestionTournoi"),
    path('createTournoi/', views.pagecreatetournoi,name="creationTournoi"),
    path('listeTournois/', views.listetournois, name="listeTournois"),
    path('gestionTournoi/createPool/', views.createPool),
    path('gestionTournoi/<str:name>/', views.listteam),
    #path('create/', views.createtournoi),
    
    #Connexion/Inscription
    path('register/', views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout")
]