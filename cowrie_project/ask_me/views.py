from django.shortcuts import render
from django.conf import settings
from django.db.models import Count
from .models import AttackType, Tips, SummaryHistory, QAHistory, ClassificationHistory
from django.contrib.auth.models import User
from django.http import JsonResponse

import requests, random
import json
import pandas as pd
import matplotlib  
import matplotlib.pyplot as plt
import io
import base64

def classification_view(request):
    matplotlib.use('Agg') 
        
    attack_type = None
    description = None
    chart_data = None
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

        backend_url = "https://stunning-silkworm-brave.ngrok-free.app/classify"  
        response = requests.post(backend_url, json=log_input)
        
        if response.status_code == 200:
            result = response.json()
            attack_type = result.get('attack_type')
            if request.user.is_authenticated:
                record = ClassificationHistory(user=request.user, input_log=json.dumps(log_input), attack_type=attack_type, actual_type=log_input['eventid'])
                record.save()
            try:
                attack_type_entry = AttackType.objects.get(attack_type=attack_type)
                description = attack_type_entry.description
            except AttackType.DoesNotExist:
                description = "No description available for this attack type."
        else:
            attack_type = "Error retrieving attack type from backend."
            description = "Please check the input or try again later."

        type_data = ClassificationHistory.objects.values('attack_type').annotate(count=Count('attack_type'))
        type_counts = pd.Series({item['attack_type']: item['count'] for item in type_data}).sort_values(ascending=False)
        try:
            fig, ax = plt.subplots(figsize=(10, 6))
            type_counts.plot(kind='bar', ax=ax, color='skyblue', alpha=0.7)
            for i, v in enumerate(type_counts):
                ax.text(i, v + 0.5, str(v), ha='center')

            if attack_type in type_counts.index:
                idx = type_counts.index.tolist().index(attack_type)
                ax.patches[idx].set_facecolor('navy')

            ax.set_xticklabels(type_counts.index, rotation=45, ha='right')  
            ax.set_xlabel("Attack Types")  
            ax.set_ylabel("Number of Occurrences")  
            ax.set_title("Proportion of Attack Types From History")  
            plt.tight_layout()

            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()
            chart_data = base64.b64encode(image_png).decode('utf-8')
        except FileNotFoundError:
            description = "Error: CSV file not found. Please contact the admin."
        except Exception as e:
            description = f"Error processing the CSV file: {str(e)}"

    return render(request, 'ask_me/classification.html', {
        'attack_type': attack_type,
        'description': description,
        'chart_data': chart_data,
        'log_input': log_input
    })
def qa_view(request):
    answer = None
    question = None
    
    tips = list(Tips.objects.all())
    tips_data = [{'content': tip.content} for tip in tips] 
    
    if request.method == 'POST':
        question = request.POST.get('question')
        backend_url = "https://stunning-silkworm-brave.ngrok-free.app/qa" 
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

        backend_url = "https://stunning-silkworm-brave.ngrok-free.app/summarize"  # Replace with your Flask backend URL
        
        try:
            response = requests.post(backend_url, json={'paragraph': paragraph})
            response.raise_for_status()
            summary = response.json().get('summary')

            if request.user.is_authenticated:
                record = SummaryHistory(user=request.user, paragraph=paragraph, summary=summary)
                record.save()
            
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            summary = "An error occurred while generating the summary. Please try again."

    return render(request, 'ask_me/summary.html', {'summary': summary, 'paragraph': paragraph})



def cHistory_view(request):
    attackTypes = [
        "cowrie.session.connect", 
        "cowrie.session.params", 
        "cowrie.direct-tcpip.data", 
        "cowrie.session.data", 
        "cowrie.session.disconnect",
        "cowrie.password.failed",
        "cowrie.password.success",
        "cowrie.system.info",
        "cowrie.shell.request",
        "cowrie.direct-tcpip.data",
        "cowrie.connection",
        "cowrie.session.shell",
        "cowrie.login.failed",
        "cowrie.login.success",
        "cowrie.exec",
        "cowrie.session.term"
    ]
    
    frequencies = [5, 3, 7, 6, 4, 9, 8, 10, 2, 3, 1, 6, 2, 3, 5, 7]
    
    # 將 0-15 範圍傳遞給模板
    range_data = range(16)
    
    # return render(request, 'ask_me/cHistory.html', {
    #     'attackTypes': attackTypes,
    #     'frequencies': frequencies,
    #     'range_data': range_data,
    # }

    # 合併 attackTypes 和 frequencies
    attack_data = [{'attackType': attackTypes[i], 'frequency': frequencies[i]} 
                   for i in range(len(attackTypes))]
    
    # If you want to include historical records for each attack type, add that logic here:
    # Example (mocked records):
    for item in attack_data:
        item["records"] = [{"time": "2024-11-29 06:00:00", "input_log": "Sample log"}]  # Replace with actual records from your database


    return render(request, 'ask_me/cHistory.html', {
        'attack_data': attack_data,
    })