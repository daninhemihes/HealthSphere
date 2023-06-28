from rest_framework.views import APIView
from rest_framework.response import Response
from HealthSpace.serializer import UserSerializer
from HealthSpace.models import tbUser
from HealthSpace.api_views.crypto import create


class RegisterUser(APIView):
    def get(self, request):
        return Response({'message':"Nada a mostrar!"},status=200)

    def post(self, request):

        if tbUser.objects.filter(username=request.data["username"]):
            return Response({"error":"Já possui registro"}, status=400)

        data = request.data
        data['password'] = create(request.data['password'])

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer._errors, status=400)

        return Response(status=201)