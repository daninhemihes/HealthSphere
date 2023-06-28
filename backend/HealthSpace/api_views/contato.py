from rest_framework.views import APIView
from rest_framework.response import Response
from HealthSpace.models import tbEmergencyContact
from HealthSpace.serializer import EmergencyContactSerializer


class ContatoEmergencia(APIView):
    def get(self, request, username):
        retorno_dados = []
        tabela_contato = tbEmergencyContact.objects.filter(username=username)
        for cada_contato_emergencia in tabela_contato:
            retorno_dados.append({
                'name':cada_contato_emergencia.name,
                'relationship': cada_contato_emergencia.relationship,
                'phone':cada_contato_emergencia.phone,
            })
        return Response(retorno_dados, status=200)

    def post(self, request):
        data = request.data
        serializer = EmergencyContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer._errors, status=400)

        return Response(status=201)
    
    def delete(self, request):
        try:
            tbEmergencyContact.objects.get(username=request.data["username"], phone=request.data["phone"]).delete()
        except:
            return Response(status=404)
        
        return Response(status=201)