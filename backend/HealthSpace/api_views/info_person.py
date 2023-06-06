from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from HealthSpace.models import tbPerson
from HealthSpace.serializer import PersonSerializer


class InfoPerson(APIView):
    def get(self, request, pk):
        dados_usuario = get_object_or_404(tbPerson, pk=pk)
        return Response(dados_usuario, status=200)

    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer._errors, status=400)

        return Response(status=201)
    
    def put(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer._errors, status=400)

        return Response(status=201)