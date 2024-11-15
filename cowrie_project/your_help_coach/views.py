from django.shortcuts import render
import requests
import logging
from .models import CowrieLogAttack
from ask_me.models import ClassificationHistory

def attack_suggestion_view(request):
    attack_type = None
    
    if request.method == 'POST':
        fields = ['username', 'input', 'protocol', 'duration', 'data', 'keyAlgs', 'message', 'eventid', 'kexAlgs']
        
        data = {field: request.POST.get(field, 'nan') or 'nan' for field in fields}

        backend_url = "https://ewe-happy-centrally.ngrok-free.app/classify"  # Replace with your Flask backend URL
        response = requests.post(backend_url, json=data)

        if response.status_code == 200:
            result = response.json()
            attack_type = result.get('attack_type')

            if request.user.is_authenticated:
                record = ClassificationHistory(
                    user = request.user, attack_type = attack_type, 
                    username = data["username"], input = data["input"], protocol = data["protocol"], 
                    duration = data["duration"], dataAttr = data["data"], keyAlgs = data["keyAlgs"], 
                    message = data["message"], eventid = data["eventid"], kexAlgs = data["kexAlgs"]
                )
                record.save()

        else:
            attack_type = "Error retrieving attack type from backend."
            
    return render(request, 'your_help_coach/attack_suggestion.html', {
        'attack_type': attack_type
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
