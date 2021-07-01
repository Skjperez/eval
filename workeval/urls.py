from django.urls import path
from .views import CreateTemplate

urlpatterns = [
    path('create/', CreateTemplate, name='create_template'),
]