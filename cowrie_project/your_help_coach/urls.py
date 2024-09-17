from django.contrib import admin
from django.urls import path
from . import views

app_name = 'your_help_coach'

urlpatterns = [
    path('classify_log/', views.classify_log_view, name="classify_log"),
    path('attack_suggestion/', views.attack_suggestion_view, name="attack_suggestion"),
]