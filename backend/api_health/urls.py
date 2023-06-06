from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

#define os metodos de padrão http (get,post,...)
route = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('rest_framework.urls'))
    path('api/', include('HealthSpace.urls')),
    #aparentemente esse aqui determina que todas as urls a baixo dela serão no padrão http
    path('api/', include(route.urls)),
]