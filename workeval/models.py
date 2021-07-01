from django.db import models

# Create your models here.

class EvaluationTemplate(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 



class EvaluationTemplateQuestion(models.Model):
    evaluation_template = models.ForeignKey(EvaluationTemplate, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question 


