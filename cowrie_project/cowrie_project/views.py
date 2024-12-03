from django.http import HttpResponse
from django.shortcuts import render

def homepage_view(request):
     marquee_left = [
        "cowrie.session.params: Collected 1968 records.",
        "cowrie.session.file_upload: Collected 175 records.",
        "cowrie.session.file_download.failed: Collected 243 records.",
        "cowrie.session.file_download: Collected 111 records.",
        "cowrie.session.closed: Collected 7973 records.",
        "cowrie.login.success: Collected 3531 records.",
        "cowrie.login.failed: Collected 2316 records.",
        "cowrie.log.closed: Collected 1839 records.",
        "cowrie.direct-tcpip.request: Collected 4388 records.",
        "cowrie.direct-tcpip.data: Collected 341 records.",
        "cowrie.command.input: Collected 2033 records.",
        "cowrie.command.failed: Collected 190 records.",
        "cowrie.client.version: Collected 98 records.",
        "cowrie.client.size: Collected 76 records.",
        "cowrie.client.kex: Collected 6650 records.",
        "cowrie.session.connect: Collected 8419 records.",
        "Collected 643 records in the past 7 days.",
        "Collected an average of 2957 records per month."
    ]
     marquee_right = [
        "cowrie.direct-tcpip.data: Collected 341 records.",
        "cowrie.command.input: Collected 2033 records.",
        "cowrie.command.failed: Collected 190 records.",
        "cowrie.client.version: Collected 98 records.",
        "cowrie.client.size: Collected 76 records.",
        "cowrie.client.kex: Collected 6650 records.",
        "cowrie.session.connect: Collected 8419 records.",
        "Collected 643 records in the past 7 days.",
        "Collected an average of 2957 records per month.",
        "cowrie.session.params: Collected 1968 records.",
        "cowrie.session.file_upload: Collected 175 records.",
        "cowrie.session.file_download.failed: Collected 243 records.",
        "cowrie.session.file_download: Collected 111 records.",
        "cowrie.session.closed: Collected 7973 records.",
        "cowrie.login.success: Collected 3531 records.",
        "cowrie.login.failed: Collected 2316 records.",
        "cowrie.log.closed: Collected 1839 records.",
        "cowrie.direct-tcpip.request: Collected 4388 records."

    ]
     return render(request, 'home.html', {'marquee_left': marquee_left, 'marquee_right': marquee_right})


def about_view(request):
    return render(request, 'about.html')
