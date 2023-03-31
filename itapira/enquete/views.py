from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Cheia de mania, toda dengosa, digui digui ieeee")

def valkor(request):
    return HttpResponse("Biosyn Industries")


