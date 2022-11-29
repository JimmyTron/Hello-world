from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Stori
# Create your views here.

def stori_list(request):
    MAX_OBJECTS = 20
    mastori = Stori.objects.all()[:MAX_OBJECTS]
    data = {"results": list(mastori.values("stori","created_by__user","created"))}
    return JsonResponse(data)

def stori_detail(request, pk):
    stori = get_object_or_404(Stori, pk=pk)
    data = {"results": {
        "stori_title": stori.title,
        "created_by": stori.created_by.Account,
        "created": stori.created
    }}
    return JsonResponse(data)