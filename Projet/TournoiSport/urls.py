from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('gestionTournoi/', views.gestionTournoi),
    path('createTournoi/', views.pagecreatetournoi),
    path('listeTournois/', views.listetournois),
    path('gestionTournoi/createPool/', views.createPool),
    path('gestionTournoi/<str:name>/', views.listteam),
    path('create/', views.createtournoi)
]