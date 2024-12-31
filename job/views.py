from django.shortcuts import render
from .serializars import *
from .models import *
from rest_framework import viewsets
from rest_framework import filters
from django.db.models import Q

class EmployeePostJobIndivitual(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        employe_id = request.query_params.get("employer_id")
        if employe_id:
            return query_set.filter(employer=employe_id)
        return query_set
    
class IndivitualJob(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        job_id = request.query_params.get("job_id")
        if job_id:
            return query_set.filter(id=job_id)
        return query_set

class SearchByCategory(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        category_name = request.query_params.get("search")
        if category_name:
            return query_set.filter(category__categorie__icontains=category_name)
        return query_set
    
class SearchByCompany(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        company_name = request.query_params.get("company")
        if company_name:
            return query_set.filter(company__name__icontains=company_name)
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
    filter_backends = [EmployeePostJobIndivitual, IndivitualJob, SearchByCategory, SearchByCompany]
