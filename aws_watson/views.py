from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Requests

# Create your views here.
@csrf_exempt
def test(request):
    if request.method == 'POST':
        text = request.POST.get("text", 1)
        request_create = Requests.objects.create(
                request_text=text,
                )
        return HttpResponse(text)
    else:
        requests = Requests.objects.all()

        return render(request, 'aws_watson/show.html', {'requests': requests, })
