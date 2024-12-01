from django.http import HttpResponse
from django.shortcuts import render

def homepage_view(request):
     marquee_left = [
        "cowrie.session.params：共蒐集到 1968 條資料。",
        "cowrie.session.file_upload：共蒐集到 175 條資料。",
        "cowrie.session.file_download.failed：共蒐集到 243 條資料。",
        "cowrie.session.file_download：共蒐集到 111 條資料。",
        "cowrie.session.closed：共蒐集到 7973 條資料。",
        "cowrie.login.success：共蒐集到 3531 條資料。",
        "cowrie.login.failed：共蒐集到 2316 條資料。",
        "cowrie.log.closed：共蒐集到 1839 條資料。",
        "cowrie.direct-tcpip.request：共蒐集到 4388 條資料。",
        "cowrie.direct-tcpip.data：共蒐集到 341 條資料。",
        "cowrie.command.input：共蒐集到 2033 條資料。",
        "cowrie.command.failed：共蒐集到 190 條資料。",
        "cowrie.client.version：共蒐集到 98 條資料。",
        "cowrie.client.size：共蒐集到 76 條資料。",
        "cowrie.client.kex：共蒐集到 6650 條資料。",
        "cowrie.session.connect：共蒐集到 8419 條資料。",
        "最近 7 天共蒐集到 643 條資料。",
        "每個月平均蒐集到 2957 條資料。"
    ]
     marquee_right = [
        "cowrie.command.failed：共蒐集到 190 條資料。",
        "cowrie.client.version：共蒐集到 98 條資料。",
        "cowrie.client.size：共蒐集到 76 條資料。",
        "cowrie.client.kex：共蒐集到 6650 條資料。",
        "cowrie.session.connect：共蒐集到 8419 條資料。",
        "最近 7 天共蒐集到 643 條資料。",
        "每個月平均蒐集到 2957 條資料。",
        "cowrie.session.params：共蒐集到 1968 條資料。",
        "cowrie.session.file_upload：共蒐集到 175 條資料。",
        "cowrie.session.file_download.failed：共蒐集到 243 條資料。",
        "cowrie.session.file_download：共蒐集到 111 條資料。",
        "cowrie.session.closed：共蒐集到 7973 條資料。",
        "cowrie.login.success：共蒐集到 3531 條資料。",
        "cowrie.login.failed：共蒐集到 2316 條資料。",
        "cowrie.log.closed：共蒐集到 1839 條資料。",
        "cowrie.direct-tcpip.request：共蒐集到 4388 條資料。",
        "cowrie.direct-tcpip.data：共蒐集到 341 條資料。",
        "cowrie.command.input：共蒐集到 2033 條資料。"

    ]
     return render(request, 'home.html', {'marquee_left': marquee_left, 'marquee_right': marquee_right})


def about_view(request):
    return render(request, 'about.html')
