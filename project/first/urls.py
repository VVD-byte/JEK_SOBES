from django.urls import path
from .views import FirstTask, WatchJson

urlpatterns = [
    path('', FirstTask.as_view(), name='FirstTask'),
    path('<num>/', WatchJson.as_view(), name='WatchJson')
]