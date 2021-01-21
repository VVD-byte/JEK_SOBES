from django.urls import path
from .views import SecondTask

urlpatterns = [
    path('', SecondTask),
]