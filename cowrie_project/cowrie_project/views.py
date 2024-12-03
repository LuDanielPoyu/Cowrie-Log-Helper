from django.shortcuts import render
from django.db.models import Count
from ask_me.models import ClassificationHistory

import pandas as pd

def homepage_view(request):
    type_data = ClassificationHistory.objects.values('attack_type') \
    .annotate(count=Count('attack_type'))
    type_counts = pd.Series({item['attack_type']: item['count'] for item in type_data}).sort_values(ascending=False)
    
    marquee_left = []
    for att_type, att_count in type_counts.items():
        marquee_left.append(f'{att_type}: Collected {att_count} records.')
        
    marquee_left.append("Collected 643 records in the past 7 days.")
    marquee_left.append("cowrie.session.connect: Collected 8419 records.")
    marquee_right = marquee_left[::-1]
    
    return render(request, 'home.html', {'marquee_left': marquee_left, 'marquee_right': marquee_right})


def about_view(request):
    return render(request, 'about.html')
