from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    cv = serializers.SerializerMethodField()
    class Meta:
        model = JobApplication
        fields = '__all__'
    
    def get_cv(self, obj):
        return obj.cv.url if obj.cv else None