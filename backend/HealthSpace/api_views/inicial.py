from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPI(APIView):
    def get(self, request):
        mensagem = 'Olá'
        return Response(mensagem)