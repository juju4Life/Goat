from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["GET", "POST", ])
def daily_mtg_hook(request):
    print(request.body)
    print(request.GET)
    print(request.POST)
    print(request.method)
    print(request.encoding)
    print(request.META)
    print(request.headers)
    print(request.read())
    print(request.read_line())
    challenge = request.GET.get("hub.challenge")
    topic = request.GET.get("hub.topic")

    return HttpResponse(challenge)


