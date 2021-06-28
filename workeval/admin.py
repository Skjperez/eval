from django.contrib import admin
from .models import EvaluationTemplate, EvaluationTemplateQuestion

# Register your models here.

class EvaluationTemplateAdmin(admin.ModelAdmin):
    fields = ['name']
    readonly_fields = ['created_at', 'updated_at']

class EvaluationTemplateQuestionAdmin(admin.ModelAdmin):
    fields = ['evaluation_template', 'question']

admin.site.register(EvaluationTemplate, EvaluationTemplateAdmin)
admin.site.register(EvaluationTemplateQuestion, EvaluationTemplateQuestionAdmin)
    
    



