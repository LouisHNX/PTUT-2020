from django.contrib import admin
from .models import team,pool,phase#,tournament

admin.site.register(team)
admin.site.register(pool)
admin.site.register(phase)
#admin.site.register(tournament)

