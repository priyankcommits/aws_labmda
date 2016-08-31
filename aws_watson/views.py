from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def test(request):
    text = request.POST.get("text", 1)
    return HttpResponse(text)
