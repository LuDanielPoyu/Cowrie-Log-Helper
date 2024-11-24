from django.contrib import admin
from .models import AttackType, Tips, SummaryHistory, QAHistory, ClassificationHistory
# Register your models here.

@admin.register(AttackType)
class AttackTypeAdmin(admin.ModelAdmin):
    list_display = ('attack_type', 'description')

@admin.register(Tips)
class TipsAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ('content',)
    
@admin.register(ClassificationHistory)
class ClassificationHistory(admin.ModelAdmin):
    list_display = ('id', 'user', 'timestamp', 'input_log', 'attack_type', 'actual_type')
    search_fields = ('id',)
    
@admin.register(QAHistory)
class QAHistory(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'question', 'answer')
    
@admin.register(SummaryHistory)
class SummaryHistory(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'paragraph', 'summary')
    
