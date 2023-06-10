from django.urls import path
from HealthSpace.api_views.login import LoginUser
from HealthSpace.api_views.register import RegisterUser
from HealthSpace.api_views.info_person import InfoPerson
from HealthSpace.api_views.qrcode import QRcode
from HealthSpace.api_views.ficha import FichaMedica


urlpatterns = [
    path('login/', LoginUser.as_view()),
    path('register/', RegisterUser.as_view()),
    path('info_person/', InfoPerson.as_view()),
    path('info_person/<int:pk>/', InfoPerson.as_view()),
    path('qrcode/', QRcode.as_view()),
    path('ficha_medica/<str:hash>/', FichaMedica.as_view()),

]