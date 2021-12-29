from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def get_jitsi(request: HttpRequest) -> HttpResponse:
    return render(request, 'jitsi/jitsi.html')
