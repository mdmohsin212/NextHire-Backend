from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    cv = serializers.FileField()
    class Meta:
        model = JobApplication
        fields = '__all__'