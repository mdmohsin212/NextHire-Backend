from rest_framework import serializers
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
    # category = serializers.StringRelatedField(many=True)
    # applicants = serializers.StringRelatedField(many=True)
    class Meta:
        model = JobListing  
        fields = '__all__'