from rest_framework.views import APIView
from rest_framework.response import Response

from HealthSpace.models import tbAllergiesReactions
from HealthSpace.serializer import AllergiesReactionsSerializer


class ReacoesAlergicas(APIView):
    def get(self, request, username):
        retorno_dados = []
        tabela_alergia = tbAllergiesReactions.objects.filter(username=username)
        for cada_reacao_alergica in tabela_alergia:
            retorno_dados.append({
                'allergiesReactions': cada_reacao_alergica.allergiesReactions,
                'notes':cada_reacao_alergica.notes,
            })
        
        return Response(retorno_dados, status=200)

    def post(self, request):
        data = request.data
        serializer = AllergiesReactionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer._errors, status=400)

        return Response(status=201)

    def delete(self, request):
        try:
            tbAllergiesReactions.objects.get(username=request.data["username"], allergiesReactions=request.data["allergiesReactions"]).delete()
        except:
            return Response(status=404)
        
        return Response(status=201)    