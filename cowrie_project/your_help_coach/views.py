from django.shortcuts import render
import requests
import logging
from .models import CowrieLogAttack
# Create your views here.

def attack_suggestion_view(request):
    attack_type = None

    if request.method == 'POST':
        data = {
            'username': request.POST.get('username'),
            'input': request.POST.get('input'),
            'protocol': request.POST.get('protocol'),
            'duration': request.POST.get('duration'),
            'data': request.POST.get('data'),
            'keyAlgs': request.POST.get('keyAlgs'),
            'message': request.POST.get('message'),
            'eventid': request.POST.get('eventid'),
            'kexAlgs': request.POST.get('kexAlgs')
        }

        backend_url = "https://ewe-happy-centrally.ngrok-free.app/classify"   # Replace with your Flask backend URL
        response = requests.post(backend_url, json=data)

        if response.status_code == 200:
            result = response.json()
            attack_type = result.get('attack_type')
            
    return render(request, 'your_help_coach/attack_suggestion.html', {
        'attack_type': attack_type,
    })
    
def help_coach_view(request):
    attack_type = None
    affected = None
    mitigation = None 
    solutions = None 
    learn_more_links = []  # Updated to hold links

    if request.method == 'POST':
        attack_type = request.POST.get('encounteredAttack')

        # Query for the attack type
        try:
            attack = CowrieLogAttack.objects.get(attack_name__iexact=attack_type)  # Case-insensitive search
            affected = attack.affected
            mitigation = attack.mitigation
            solutions = attack.solutions
            learn_more_links = attack.get_learn_more_links()  # Get list of learn more links
        except CowrieLogAttack.DoesNotExist:
            logging.error(f'Attack type {attack_type} not found in the database.')
            affected = "No data available for this attack type."
            mitigation = "No mitigation available."
            solutions = "No solutions available."
            learn_more_links = []

    return render(request, 'your_help_coach/help_coach.html', {
        'attack_type': attack_type,
        'affected': affected,
        'mitigation': mitigation,
        'solutions': solutions,
        'learn_more_links': learn_more_links  # Pass the links to the template
    })
