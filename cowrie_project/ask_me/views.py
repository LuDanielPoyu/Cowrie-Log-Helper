from django.shortcuts import render
import requests, random
from .models import AttackType, Tips, SummaryHistory, QAHistory, ClassificationHistory
import json
import re

# Create your views here.
def classification_view(request):
    attack_type = None
    description = None
    log_input = ""

    if request.method == 'POST':
        log_input = request.POST.get('log_input', '').strip()
        
        if not log_input.startswith('{'):
            log_input = '{' + log_input
        if not log_input.endswith('}'):
            log_input = log_input + '}'
        
        log_input = eval(log_input)

        if not log_input:
            return render(request, 'ask_me/classification.html', {
                'attack_type': "Error: No input provided.",
                'description': "Please paste a valid cowrie log row.",
                'log_input': log_input  
            })
        
        col_names = [
            "username", "input", "size", "compCS", "width", "outfile", "protocol",
            "duration", "height", "url", "keyAlgs", "ttylog", "data", "sensor",
            "arch", "session", "shasum", "message", "langCS", "timestamp",
            "kexAlgs", "encCS", "password", "version", "dst_port", "macCS",
            "destfile", "client_fingerprint", "filename", "eventid"
        ]
        
        data_dict = {col: 'nan' for col in col_names}
        
        for key, value in log_input.items():
            if key in col_names:
                data_dict[key] = value
                
        required_params = {param: data_dict.get(param, 'nan') for param in [
            'username', 'input', 'protocol', 'duration', 'data', 'keyAlgs', 'message', 'eventid', 'kexAlgs'
        ]}

        backend_url = "https://ewe-happy-centrally.ngrok-free.app/classify"  # Replace with your Flask backend URL
        response = requests.post(backend_url, json=required_params)

        if response.status_code == 200:
            result = response.json()
            attack_type = result.get('attack_type')

            if request.user.is_authenticated:
                record = ClassificationHistory(user = request.user, input_log = log_input, attack_type = attack_type)
                record.save()

            try:
                attack_type_entry = AttackType.objects.get(attack_type=attack_type)
                description = attack_type_entry.description
            except AttackType.DoesNotExist:
                description = "No description available for this attack type."
        else:
            attack_type = "Error retrieving attack type from backend."
            description = "Please check the input or try again later."

        input_log = ""  # Clear the input field

    return render(request, 'ask_me/classification.html', {
        'attack_type': attack_type,
        'description': description,
        'data_dict': locals().get('data_dict', {}),
        'log_input': log_input  
    })

def qa_view(request):
    answer = None
    question = None
    
    tips = list(Tips.objects.all())
    tips_data = [{'content': tip.content} for tip in tips] 
    
    if request.method == 'POST':
        question = request.POST.get('question')
        backend_url = "https://ewe-happy-centrally.ngrok-free.app/qa" 
        response = requests.post(backend_url, json={'question': question})

        if response.status_code == 200:
            answer = response.json().get('answer')

            if request.user.is_authenticated:
                record = QAHistory(user = request.user, question = question, answer = answer)
                record.save()

    random.shuffle(tips)

    return render(request, 'ask_me/qa.html', {
        'answer': answer, 
        'question': question, 
        'tips': json.dumps(tips_data)  
    })

def summary_view(request):
    summary = None
    paragraph = None

    if request.method == 'POST':
        paragraph = request.POST.get('paragraph')

        backend_url = "https://ewe-happy-centrally.ngrok-free.app/summarize"  # Replace with your Flask backend URL
        
        try:
            response = requests.post(backend_url, json={'paragraph': paragraph})
            response.raise_for_status()
            summary = response.json().get('summary')

            if request.user.is_authenticated:
                record = SummaryHistory(user = request.user, paragraph = paragraph, summary = summary)
                record.save()
            
        except requests.RequestException as e:
            print(f"Request failed: {e}")

    return render(request, 'ask_me/summary.html', {'summary': summary, 'paragraph': paragraph})
