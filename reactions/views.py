from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from reactions.models import Stori
# Create your views here.

def stori_list(request):
    MAX_OBJECTS = 20
    mastori = Stori.objects.all()[:MAX_OBJECTS]
    data = {"results": list(mastori.values("title","description","created_by__alias","created"))}
    return JsonResponse(data)

def stori_detail(request, pk):
    stori = get_object_or_404(Stori, pk=pk)
    data = {"results": {
        "Stori Title": stori.title,
        "Stori": stori.stori,
        "Stori Description": stori.description,
        "Stori Category": stori.category.category,
        "created by": stori.created_by.alias,# user
        "created": stori.created
    }}
    return JsonResponse(data)