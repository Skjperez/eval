from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import EvaluationTemplate

# Create your views here.


def CreateTemplate(request):
    return HttpResponse('This is the beginning of this template')
    #if request.method == 'POST':
        #form = WorkEvaluationForm(request.POST)
        #if form.is_valid():



