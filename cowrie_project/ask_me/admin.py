from django.contrib import admin
from .models import AttackType
# Register your models here.

@admin.register(AttackType)
class AttackTypeAdmin(admin.ModelAdmin):
    list_display = ('attack_type', 'description')
