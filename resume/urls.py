from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('job_apply', JobApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
