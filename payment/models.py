from django.db import models
from django.contrib.auth.models import User

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
    
    def __str__(self):
        return self.name