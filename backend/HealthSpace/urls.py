from django.urls import path
from HealthSpace.api_views.login import LoginUser
from HealthSpace.api_views.register import RegisterUser
from HealthSpace.api_views.info_person import InfoPerson

urlpatterns = [
    path('login/', LoginUser.as_view()),
    path('register/', RegisterUser.as_view()),
    path('info_person/', InfoPerson.as_view()),
    path('info_person/<int:pk>/', InfoPerson.as_view()),

]