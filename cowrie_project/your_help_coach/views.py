from django.shortcuts import render
import requests
import logging
import re
import json
from .models import CowrieLogAttack
from ask_me.models import ClassificationHistory

def attack_suggestion_view(request):
    attack_type = None
    log_input = ""

    if request.method == 'POST':
        log_input = request.POST.get('log_input', '').strip().replace("'", '"')

        if not log_input.startswith('{'):
            log_input = '{' + log_input
        if not log_input.endswith('}'):
            log_input = log_input + '}'

        try:
            log_input = json.loads(log_input)
        except json.JSONDecodeError:
            return render(request, 'ask_me/classification.html', {
                'attack_type': "Error: Invalid input format.",
                'description': "Please provide a valid JSON-formatted cowrie log row.",
                'log_input': log_input
            })

        if not log_input:
            return render(request, 'ask_me/classification.html', {
                'attack_type': "Error: No input provided.",
                'description': "Please paste a valid cowrie log row.",
                'log_input': log_input
            })

        # Send data to the Flask backend
        backend_url = "https://marten-loving-accurately.ngrok-free.app/classify"  # Replace with your Flask backend URL
        response = requests.post(backend_url, json=log_input)

        if response.status_code == 200:
            result = response.json()
            attack_type = result.get('attack_type')

            if request.user.is_authenticated:
                record = ClassificationHistory(user = request.user, input_log=json.dumps(log_input), attack_type = attack_type)
                record.save()

        else:
            attack_type = "Error retrieving attack type from backend."

    return render(request, 'your_help_coach/attack_suggestion.html', {
        'attack_type': attack_type,
        'log_input': ""  # Clear the input block after successful submission
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
            description = attack.description
            affected = attack.affected
            mitigation = attack.mitigation
            solutions = attack.solutions
            learn_more_links = attack.get_learn_more_links()  # Get list of learn more links
        except CowrieLogAttack.DoesNotExist:
            logging.error(f'Attack type {attack_type} not found in the database.')
            description = "No descriptions for this attack type."
            affected = "No data available for this attack type."
            mitigation = "No mitigation available."
            solutions = "No solutions available."
            learn_more_links = []

    return render(request, 'your_help_coach/help_coach.html', {
        'attack_type': attack_type, 
        'description': description, 
        'affected': affected, 
        'mitigation': mitigation, 
        'solutions': solutions, 
        'learn_more_links': learn_more_links  # Pass the links to the template
    })
