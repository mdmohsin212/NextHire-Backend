from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework import filters
# from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AppliedJobIndivitual(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        seeker_id = request.query_params.get("job_seeker")
        if seeker_id:
            return query_set.filter(job_seeker=seeker_id)
        return query_set

class JobApplicationViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = JobApplication.objects.all() 
    serializer_class = JobApplicationSerializer
    filter_backends = [AppliedJobIndivitual]