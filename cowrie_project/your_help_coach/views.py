from django.shortcuts import render

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

        backend_url = "https://cfd5-34-74-82-165.ngrok-free.app"  # Replace with your Flask backend URL
        response = request.post(backend_url, json=data)

        if response.status_code == 200:
            result = response.json()
            attack_type = result.get('attack_type')
            # 渲染攻擊建議頁面並傳遞 attack_type
    return render(request, 'your_help_coach/attack_suggestion.html', {'attack_type': attack_type})

def help_coach_view(request):
    attack_type = None
    affected = None  # 將來用來存放查詢到的資料
    mitigation = None 
    solutions = None 
    learn_more = None 

    if request.method == 'POST':
        # 獲取表單中的攻擊類型
        attack_type = request.POST.get('encounteredAttack')

        # 根據 attack_type 查詢 CowrieLogAttack 模型
        try:
            attack = CowrieLogAttack.objects.get(attack_name=attack_type)
            affected = attack.affected  # 獲取 affected 的值
            mitigation = attack.mitigation  # 獲取 mitigation 的值
            solutions = attack.solutions  # 獲取 solutions 的值
            learn_more = attack.learn_more  # 獲取 learn_more 的值
        except CowrieLogAttack.DoesNotExist:
            affected = "No data available for this attack type."
            mitigation = "No mitigation available."
            solutions = "No solutions available."
            learn_more = "No additional information available."

    # 將查詢結果傳遞給模板
    return render(request, 'your_help_coach/help_coach.html', {
        'attack_type': attack_type,
        'affected': affected,
        'mitigation': mitigation,
        'solutions': solutions,
        'learn_more': learn_more
    })