from rest_framework.views import APIView
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from HealthSpace.models import tbQRcode
from HealthSpace.serializer import QRcodeSerializer
from django.core.files import File
from django.http import FileResponse
import qrcode
import random
import string

def create_qr(hash):
    image = qrcode.make(f"http://localhost:5173/ficha/{hash}")
    image.save(f"C:\\VSO\\healthspace\\backend\\media\\{hash}.jpg")

def gerador_de_hash(length):
    hash = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    
    return hash


class QRcode(APIView):
    def get(self, request):
        QRcode = get_object_or_404(tbQRcode, username=request.data["username"])
        
        return FileResponse(QRcode.qrcode, content_type='image/jpeg')

    def post(self, request):
        if tbQRcode.objects.filter(username=request.data["username"]):
            return Response({'error':'QRcode já cadastrado'}, status=400) 
        
        data = request.data
        data['hash'] = gerador_de_hash(10)

        create_qr(data['hash'])

        with open(f'C:\\VSO\healthspace\\backend\\media\\{data["hash"]}.jpg', 'rb') as arquivo:
            data['qrcode'] = File(arquivo, name =f'{data["hash"]}.jpg')

            serializer = QRcodeSerializer(data=data)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        QRcode = get_object_or_404(tbQRcode, username=request.data["username"])
        QRcode.delete()
        
        return Response({'mesage':'Deletado com sucesso!'}, status=200)
