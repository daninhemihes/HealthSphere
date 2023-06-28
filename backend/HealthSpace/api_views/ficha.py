from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from HealthSpace.models import tbQRcode, tbPerson, tbEmergencyContact, tbMedicalConditions, tbAllergiesReactions


class FichaMedica(APIView):
    def get(self, request, hash):
        retorno_front = {
            'dados_person':[],
            'dados_contato':[],
            'dados_condicoes':[],
            'dados_reacoes':[]
        }
        tabela_qrcode = get_object_or_404(tbQRcode, hash=hash)
        tabela_person = tbPerson.objects.filter(username=tabela_qrcode.username).first()
        retorno_front["dados_person"].append({
            'username': tabela_person.username.pk,
            'firstName':tabela_person.firstName,
            'lastName':tabela_person.lastName,
            'sex':tabela_person.sex,
            'birthDate':tabela_person.birthDate,
            'bloodType':tabela_person.bloodType,
            'organDonor':tabela_person.organDonor,
            'weight':tabela_person.weight,
            'height':tabela_person.height,
            'maritalStatus':tabela_person.maritalStatus,
            'color':tabela_person.color,
            'nationality':tabela_person.nationality,
            'occupation':tabela_person.occupation,
            'address':tabela_person.address,
            'phone':tabela_person.phone,
            'primaryLanguague':tabela_person.primaryLanguague
        })
        
        tabela_contato_emergencia = tbEmergencyContact.objects.filter(username=tabela_qrcode.username)
        for cada_contato in tabela_contato_emergencia:
            retorno_front["dados_contato"].append({
                'name':cada_contato.name,
                'relationship':cada_contato.relationship,
                'phone': cada_contato.phone,
            })
        
        tabela_condicoes_medicas = tbMedicalConditions.objects.filter(username=tabela_qrcode.username)
        for cada_condicao in tabela_condicoes_medicas:
            retorno_front["dados_condicoes"].append({
                'medicalCondition':cada_condicao.medicalCondition,
                'note':cada_condicao.note,
            })
        
        tabela_reacoes_alergicas = tbAllergiesReactions.objects.filter(username=tabela_qrcode.username)
        for cada_reacao in tabela_reacoes_alergicas:
            retorno_front["dados_reacoes"].append({
                'allergiesReactions':cada_reacao.allergiesReactions,
                'notes':cada_reacao.notes,
            })
        return Response(retorno_front, status=200)