from rest_framework.views import APIView
from rest_framework.response import Response
from HealthSpace.models import tbMedicalConditions
from HealthSpace.serializer import MedicalConditionsSerializer


class CondicoesMedicas(APIView):
    def get(self, request, username):
        retorno_dados = []
        tabela_condicoes = tbMedicalConditions.objects.filter(username=username)
        for cada_condicao_medica in tabela_condicoes:
            retorno_dados.append({
                'medicalCondition': cada_condicao_medica.medicalCondition,
                'notes':cada_condicao_medica.note,
            })
        return Response(retorno_dados, status=200)

    def post(self, request):
        data = request.data
        serializer = MedicalConditionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer._errors, status=400)

        return Response(status=201)
    
    def delete(self, request):
        try:
            tbMedicalConditions.objects.get(username=request.data["username"], pk=request.data["medicalCondition"]).delete()
        except:
            return Response(status=404)
        
        return Response(status=201)



    