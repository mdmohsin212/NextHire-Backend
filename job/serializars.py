from rest_framework import serializers
from resume.serializers import *
from .models import *

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
        
class CompanySerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = '__all__'
    
    def get_img(self, obj):
        return f"https://nexthire-backend.onrender.com/media/{obj.img}"
        

class JobListingSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=True)
    applicants = serializers.SerializerMethodField()
    employer = serializers.StringRelatedField(many=False)
    # company = serializers.SerializerMethodField()
    
    class Meta:
        model = JobListing
        fields = '__all__'

    def get_applicants(self, obj):
        applications = obj.applications.all()
        return JobApplicationSerializer(applications, many=True).data

    def get_company(self, obj):
        return CompanySerializer(obj.company).data