from django.db import models
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.user.username} - {self.role}'
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        email_subject = f"Someone Contact with You"
        email_body = render_to_string('contact.html', {'name' : self.name, 'email' : self.email, 'message' : self.message})
            
        email = EmailMultiAlternatives(email_subject, '', to=['siam.mohsin2005@gmail.com'])
        email.attach_alternative(email_body, "text/html")
        email.send()