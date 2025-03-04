from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Contact

ROLE_CHOICES = [
    ('Employer', 'Employer'),
    ('Job Seeker', 'Job Seeker'),
]

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = "__all__"
        
    def get_user(self, obj):
        user = obj.user
        profile = user.profile
        return {
            "id" : user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }

    

class UserRegistrationSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    role = serializers.ChoiceField(choices=ROLE_CHOICES, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        role = self.validated_data['role']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'Error': "This email already exists"})

        if password != password2:
            raise serializers.ValidationError({'Error': "Your Password doesn't match"})

        account = User(username=username, first_name=first_name, last_name=last_name, email=email)
        account.set_password(password)
        account.is_active = False
        account.save()
        Profile.objects.create(user=account, role=role)
        return account


class UserLoginSerializers(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"