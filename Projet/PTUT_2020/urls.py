from django.contrib import admin
from django.urls import path, include
from TournoiSport.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TournoiSport.urls'))
]
