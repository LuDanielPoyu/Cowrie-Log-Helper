from django.contrib import admin
from .models import CowrieLogAttack
# Register your models here.
@admin.register(CowrieLogAttack)
class CowrieLogAttackAdmin(admin.ModelAdmin):
    list_display = ('attack_name', 'description','affected', 'mitigation', 'solutions', 'learn_more')  
    search_fields = ('attack_name',) 
