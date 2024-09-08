from django.shortcuts import render

# Create your views here.
def classification_view(request):
    return render(request, 'ask_me/classification.html')

def qa_view(request):
    return render(request, 'ask_me/qa.html')

def summary_view(request):
    return render(request, 'ask_me/summary.html')