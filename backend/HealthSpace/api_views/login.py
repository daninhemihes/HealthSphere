from rest_framework.views import APIView
from HealthSpace.api_views. crypto import compare_password
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from HealthSpace.models import tbUser


# Classe para validar se o usuário existe no banco de dados
class LoginUser(APIView):
    def get(self, request):
        return Response({'message':'Nada para exibir'}, status=200)
    
    def post(self, request):
        email = request.data['email']
        usuario = request.data['username']
        senha = request.data['password']

        if email:
            user_filtered = tbUser.objects.filter(email=email)
            user_filtered = get_object_or_404(tbUser, email=email)
            
            if compare_password(senha, user_filtered.password):
                return Response(user_filtered.username, status=200)
            else: 
                return Response(False, status=203)
            
        else:
            user_filtered = get_object_or_404(tbUser, username=usuario)
        
        if compare_password(senha, user_filtered.password):
            return Response(user_filtered.username, status=200)
        else: 
            return Response(False, status=203)