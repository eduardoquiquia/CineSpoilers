from django.contrib import admin
from .models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'genre', 'profile_url')
    
    list_filter = ('genre',)
    
    search_fields = ('name',)
    
    list_editable = ('birth_year',)