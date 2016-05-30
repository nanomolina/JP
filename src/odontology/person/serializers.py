from rest_framework import serializers
from person.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
