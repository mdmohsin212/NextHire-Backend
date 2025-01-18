from django.shortcuts import render
from .serializars import *
from .models import *
from rest_framework import viewsets
from rest_framework import filters

class AllSearch(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        employe_id = request.query_params.get("employer_id")
        if employe_id:
            return query_set.filter(employer=employe_id)
    
        job_id = request.query_params.get("job_id")
        if job_id:
            return query_set.filter(id=job_id)
        
        company_name = request.query_params.get("company")
        if company_name:
            return query_set.filter(company__name__icontains=company_name)
    
        job_type = request.query_params.get("job_type")
        if job_type:
            return query_set.filter(job_type__iexact=job_type)
        
        job_seeker = request.query_params.get("seeker_id")
        if job_seeker:
            return query_set.filter(applicants=job_seeker)
        
        return query_set

class AppliedJobSearch(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        job_id = request.query_params.get("job_id")
        if job_id:
            return query_set.filter(job__id=job_id)
        return query_set
    
class AppliedJobViewSet(viewsets.ModelViewSet):
    queryset = AppliedJob.objects.all()
    serializer_class = AppliedJobSerializer
    filter_backends = [AppliedJobSearch]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    filter_backends = [AllSearch]
