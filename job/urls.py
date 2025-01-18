from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('list', JobListingViewSet)
router.register('company', CompanyViewSet)
router.register('applied_job', AppliedJobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]   
