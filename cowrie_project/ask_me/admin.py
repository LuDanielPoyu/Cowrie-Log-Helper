from django.contrib import admin
from .models import AttackType, Tips
# Register your models here.

@admin.register(AttackType)
class AttackTypeAdmin(admin.ModelAdmin):
    list_display = ('attack_type', 'description')

@admin.register(Tips)
class TipsAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ('content',)