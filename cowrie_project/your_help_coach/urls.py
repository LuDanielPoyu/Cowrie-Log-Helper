from django.contrib import admin
from django.urls import path
from . import views

app_name = 'your_help_coach'

urlpatterns = [
    path('attack_suggestion/', views.attack_suggestion_view, name="attack_suggestion"),
    path('help_coach/', views.help_coach_view, name="help_coach"),
]