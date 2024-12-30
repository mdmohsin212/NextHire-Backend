from rest_framework import serializers
from resume.serializers import *
from .models import *

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class JobListingSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    applicants = serializers.SerializerMethodField()
    employer = serializers.StringRelatedField(many=False)
    company = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = JobListing
        fields = '__all__'

    def get_applicants(self, obj):
        applications = obj.applications.all()
        return JobApplicationSerializer(applications, many=True).data
