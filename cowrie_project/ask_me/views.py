from django.shortcuts import render
import requests, random
from .models import AttackType, Tips, SummaryHistory, QAHistory, ClassificationHistory
import json

def classification_view(request):
    attack_type = None
    description = None
    
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
