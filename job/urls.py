from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('list', JobListingViewSet)
router.register('categories', CategoriesViewSet)
router.register('company', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]   
