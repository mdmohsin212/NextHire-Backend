from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    job = serializers.StringRelatedField()
    job_seeker = serializers.StringRelatedField()
    class Meta:
        model = JobApplication
        fields = '__all__'