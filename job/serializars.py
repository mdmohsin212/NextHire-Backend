from rest_framework import serializers
from resume.serializers import *
from .models import *

        
class CompanySerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = '__all__'
    
    def get_img(self, obj):
        return f"https://nexthire-backend.onrender.com/media/{obj.img}"
        

class JobListingSerializer(serializers.ModelSerializer):
    company_img = serializers.SerializerMethodField()
    class Meta:
        model = JobListing
        fields = '__all__'

    def get_company_img(self, obj):
        return CompanySerializer(obj.company).data.get('img')
    
    
class AppliedJobSerializer(serializers.ModelSerializer):
    candidate = serializers.SerializerMethodField()
    class Meta:
        model = AppliedJob
        fields = "__all__"
    
    def get_candidate(self, obj):
        job_application = JobApplication.objects.get(job_seeker=obj.candidate, job=obj.job)
        return JobApplicationSerializer(job_application).data