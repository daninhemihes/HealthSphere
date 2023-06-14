from django.urls import path
from HealthSpace.api_views.login import LoginUser
from HealthSpace.api_views.register import RegisterUser
from HealthSpace.api_views.info_person import InfoPerson
from HealthSpace.api_views.qrcode import QRcode
from HealthSpace.api_views.ficha import FichaMedica
from HealthSpace.api_views.reacoes_alergicas import ReacoesAlergicas
from HealthSpace.api_views.condicoes import CondicoesMedicas
from HealthSpace.api_views.contato import ContatoEmergencia


urlpatterns = [
    path('login/', LoginUser.as_view()),
    path('register/', RegisterUser.as_view()),
    path('info_person/', InfoPerson.as_view()),
    path('info_person/<str:username>/', InfoPerson.as_view()),
    path('qrcode/', QRcode.as_view()),
    path('ficha_medica/<str:hash>/', FichaMedica.as_view()),
    path('reacoes_alergicas/', ReacoesAlergicas.as_view()),
    path('reacoes_alergicas/<str:username>/', ReacoesAlergicas.as_view()),
    path('condicoes_medical/', CondicoesMedicas.as_view()),
    path('condicoes_medical/<str:username>/', CondicoesMedicas.as_view()),
    path('contato_emergencia/', ContatoEmergencia.as_view()),
    path('contato_emergencia/<str:username>/', ContatoEmergencia.as_view()),

]