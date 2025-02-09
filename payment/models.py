from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'profile__role': 'Job Seeker'})
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.user.username} have {self.balance}"
    
    
class Checkout(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender", limit_choices_to={'profile__role': 'Employer'})
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver", limit_choices_to={'profile__role': 'Job Seeker'})
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=50)
    Order = models.BooleanField(default=False)  
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
    tran_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name