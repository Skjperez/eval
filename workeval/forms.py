from django import forms

class EvaluationTemplateForm(forms.Form):
    name = forms.CharField(max_length=50)