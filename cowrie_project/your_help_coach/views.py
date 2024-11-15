from django.shortcuts import render
import requests
import logging
import re
from .models import CowrieLogAttack
from ask_me.models import ClassificationHistory

def attack_suggestion_view(request):
    attack_type = None
    log_input = ""

    if request.method == 'POST':
        # Get the pasted log input
        log_input = request.POST.get('log_input', '').strip()
        if not log_input:
            return render(request, 'your_help_coach/attack_suggestion.html', {
                'attack_type': "Error: No input provided.",
                'log_input': log_input  # Retain input if there was an error
            })

        # Define column names based on the input data structure
        col_names = [
            "username", "input", "size", "compCS", "width", "outfile", "protocol",
            "duration", "height", "url", "keyAlgs", "ttylog", "data", "sensor",
            "arch", "session", "shasum", "message", "langCS", "timestamp",
            "kexAlgs", "encCS", "password", "version", "dst_port", "macCS",
            "destfile", "client_fingerprint", "filename", "eventid"
        ]

        # Regex pattern to split input while preserving lists, strings, and spaces
        regex_pattern = r"(\[[^\]]*\]|'[^']*'|\"[^\"]*\"|\S+)"
        fields = re.findall(regex_pattern, log_input)

        # Clean up the fields (strip whitespace and replace empty fields with 'nan')
        fields = [field.strip() if field.strip() else 'nan' for field in fields]

        # Ensure the number of fields matches the number of columns
        if len(fields) < len(col_names):
            fields.extend(['nan'] * (len(col_names) - len(fields)))  # Pad with 'nan'
        elif len(fields) > len(col_names):
            fields = fields[:len(col_names)]  # Truncate extra fields

        # Create a dictionary mapping column names to their corresponding values
        data_dict = dict(zip(col_names, fields))

        # Extract the required parameters for the backend
        required_params = {param: data_dict.get(param, 'nan') for param in [
            'username', 'input', 'protocol', 'duration', 'data', 'keyAlgs', 'message', 'eventid', 'kexAlgs'
        ]}

        # Send data to the Flask backend
        backend_url = "https://ewe-happy-centrally.ngrok-free.app/classify"  # Replace with your Flask backend URL
        response = requests.post(backend_url, json=required_params)

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
