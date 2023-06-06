from django.urls import path
from HealthSpace.api_views.inicial import HelloAPI

urlpatterns = [
    path('inicial/', HelloAPI.as_view()),
]