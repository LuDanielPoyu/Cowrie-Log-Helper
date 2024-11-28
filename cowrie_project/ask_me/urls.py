from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ask_me'

urlpatterns = [
    path('classification/', views.classification_view, name="classification"),
    path('qa/', views.qa_view, name="qa"),
    path('summary/', views.summary_view, name="summary"),
    path('cHistory/', views.cHistory_view, name="cHistory"),
]
