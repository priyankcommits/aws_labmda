from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Requests

import requests as req

# Create your views here.
@csrf_exempt
def test(request):
    if request.method == 'POST':
        text = request.POST.get("text", 1)
        request_create = Requests.objects.create(
                request_text=text,
                )
        res = req.post("https://hooks.slack.com/services/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",
                    data={"channel": "#general",
                        "username": "webhookbot",
                        "text": "You said" + text + "nigga",
                        "icon_emoji": ":ghost:"}
                )
        return HttpResponse(text)
    else:
        requests = Requests.objects.all()

        return render(request, 'aws_watson/show.html', {'requests': requests, })
