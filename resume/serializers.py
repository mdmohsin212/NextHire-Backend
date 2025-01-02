from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
    
    def get_cv(self, obj):
        return f"https://nexthire-backend.onrender.com/media/{obj.cv}"