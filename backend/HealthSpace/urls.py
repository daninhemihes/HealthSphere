from django.urls import path
from HealthSpace.api_views.login import LoginUser
from HealthSpace.api_views.register import RegisterUser

urlpatterns = [
    path('login/', LoginUser.as_view()),
    path('register/', RegisterUser.as_view()),

]