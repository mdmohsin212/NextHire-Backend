from rest_framework import serializers
from resume.serializers import *
from .models import *

        
class CompanySerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()   
    class Meta:
        model = Company
        fields = '__all__'
    
    def get_img(self, obj):
        return obj.img.url if obj.img else None
        

class JobListingSerializer(serializers.ModelSerializer):
    company_img = serializers.SerializerMethodField()
    class Meta:
        model = JobListing
        fields = '__all__'

    def get_company_img(self, obj):
        return CompanySerializer(obj.company).data.get('img')
    
    
class AppliedJobSerializer(serializers.ModelSerializer):
    candidate = serializers.SerializerMethodField()
    job = serializers.SerializerMethodField()

    class Meta: 
        model = AppliedJob
        fields = "__all__"
    
    def get_candidate(self, obj):
        job_applications = JobApplication.objects.filter(job_seeker=obj.candidate, job=obj.job)
        if job_applications.exists():
            return JobApplicationSerializer(job_applications.first()).data
        return None
    
    def get_job(self, obj):
        return JobListingSerializer(obj.job).data