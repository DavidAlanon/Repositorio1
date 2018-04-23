from django.contrib import admin
from fightgame.models import *

class FighterAdmin(admin.ModelAdmin):
   list_display = ['alias' , 'skills' , 'force', 'resistance']

class TournamentAdmin(admin.ModelAdmin):
   list_display = ['name' , 'start_date' , 'end_date' , 'category']

class CombatAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'tournament' , 'date', 'winner']



admin.site.register(Fighter, FighterAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Combat, CombatAdmin)