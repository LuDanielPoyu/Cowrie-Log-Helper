from django.shortcuts import render
import requests, random, time
from django.http import JsonResponse
from .models import AttackType, Tips
import json

# Create your views here.

def classification_view(request):
    attack_type = None
    description = None
    
    if request.method == 'POST':
        # Collect form data and assign "nan" to any field that is empty
        fields = ['username', 'input', 'protocol', 'duration', 'data', 'keyAlgs', 'message', 'eventid', 'kexAlgs']
        
        # Create the data dictionary, assigning "nan" to empty fields
        data = {field: request.POST.get(field, 'nan') or 'nan' for field in fields}

        # Send the request to the backend with the data
        backend_url = "https://ewe-happy-centrally.ngrok-free.app/classify"  # Replace with your Flask backend URL
        response = requests.post(backend_url, json=data)

        if response.status_code == 200:
            result = response.json()
            attack_type = result.get('attack_type')

            # Look up the description from the database
            try:
                attack_type_entry = AttackType.objects.get(attack_type=attack_type)
                description = attack_type_entry.description
            except AttackType.DoesNotExist:
                description = "No description available for this attack type."
        else:
            attack_type = "Error retrieving attack type from backend."

    return render(request, 'ask_me/classification.html', {'attack_type': attack_type, 'description': description})


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
        except requests.RequestException as e:
            print(f"Request failed: {e}")

    return render(request, 'ask_me/summary.html', {'summary': summary, 'paragraph': paragraph})
