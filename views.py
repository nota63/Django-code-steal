from django.http import HttpResponse
from django.shortcuts import render
import requests


def source_code(request):
    html = ''
    if request.method == "POST":
        a = request.POST.get('url1')
        r = requests.get(a)
        html = r.text

    return render(request, 'url.html', {'html': html})
