from django.shortcuts import redirect
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import viewsets
from rest_framework import filters
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class userSearch(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        employe_id = request.query_params.get("id")
        if employe_id:
            return query_set.filter(user__id=employe_id)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer    
    filter_backends = [userSearch]

class UserRegistationView(APIView):
    serializer_class = UserRegistrationSerializers
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            link = f"https://nexthire-backend.onrender.com/user/active/{uid}/{token}"

            email_subject = "Active your Account"
            email_body = render_to_string('confirmation_mail.html',{'confirm_link' : link, 'user' : user})
            
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializers(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'user_id': user.id,
                    'role': user.profile.role
                })
            return Response({'error': 'Invalid Credentials'}, status=400)
        return Response(serializer.errors, status=400)
    
class UserLogoutView(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
    
def active_user(request, uid64, token):
    try:
        uid_token = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid_token)
    except(User.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("https://nexthire-frontend.onrender.com/login")
    else:
        return redirect('https://nexthire-frontend.onrender.com/signup')
    
class PasswordChangeAPIView(APIView):
    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        
        if not user.check_password(old_password):
            return Response({"error": "Old password is incorrect."})
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        return Response({"message": "Password changed successfully."})
    

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers