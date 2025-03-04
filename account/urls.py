from django.urls import path, include
from .views import *
from .serializers import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('change_password/<int:user_id>/', PasswordChangeAPIView.as_view(), name='change_password'),
    path('active/<uid64>/<token>/', active_user, name='active_user'),
]
