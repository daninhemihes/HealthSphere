from rest_framework import serializers
from .models import *

## models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbUser
        fields = '__all__'
    

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbPerson
        fields = '__all__'

class MedicalConditions(serializers.ModelSerializer):
    class Meta:
        model = tbMedicalConditions
        fields = '__all__'

class AllergiesReactions(serializers.ModelSerializer):
    class Meta:
        model = tbAllergiesReactions
        fields = '__all__'

class EmergencyContact(serializers.ModelSerializer):
    class Meta:
        model = tbEmergencyContact
        fields = '__all__'