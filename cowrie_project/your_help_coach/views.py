from django.shortcuts import render

# Create your views here.
def classify_log_view(request):
    return render(request, 'your_help_coach/classify_log.html')

def attack_suggestion_view(request):
    return render(request, 'your_help_coach/attack_suggestion.html')

