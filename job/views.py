from django.shortcuts import render
from .serializars import *
from .models import *
from rest_framework import viewsets
from rest_framework import filters

class AllSearch(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        employe_id = request.query_params.get("employer_id")
        if employe_id:
            return query_set.filter(employer__iexact=employe_id)
    
        job_id = request.query_params.get("job_id")
        if job_id:
            return query_set.filter(id=job_id)
        
        category_name = request.query_params.get("search")
        if category_name:
            return query_set.filter(category__categorie__icontains=category_name)
        
        company_name = request.query_params.get("company")
        if company_name:
            return query_set.filter(company__name__icontains=company_name)
    
        job_type = request.query_params.get("job_type")
        if job_type:
            return query_set.filter(job_type__iexact=job_type)
        
        return query_set

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    filter_backends = [AllSearch]
