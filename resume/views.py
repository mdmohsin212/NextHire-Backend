from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import AllowAny
# Create your views here.

class AppliedJobIndivitual(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        seeker_id = request.query_params.get("job_seeker")
        if seeker_id:
            return query_set.filter(job_seeker=seeker_id)
        
        job_id = request.query_params.get("job_id")
        if job_id:
            return query_set.filter(job=job_id)
        
        return query_set

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all() 
    serializer_class = JobApplicationSerializer
    filter_backends = [AppliedJobIndivitual]
    permission_classes = [AllowAny]