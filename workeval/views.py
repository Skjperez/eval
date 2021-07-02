from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import EvaluationTemplate
from .forms import EvaluationTemplateForm

# Create your views here.


def CreateTemplate(request):
    if request.method == 'POST':
        form = EvaluationTemplateForm(request.POST)
        if form.is_valid():
            item = EvaluationTemplate(
             name=form.cleaned_data['name'],   
            )
            item.save()
            return redirect('/workeval/create/')
    else:
        form = EvaluationTemplateForm()
        context = {
            'form' : form
    }
        return render(request, 'workeval/createtemplate.html', context)



