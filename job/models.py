from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    img = models.ImageField(upload_to='company/', blank=True, null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

CHOICES = [
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Remote', 'Remote'),
]

class JobListing(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_listing', limit_choices_to={'profile__role': 'Employer'})
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # category = models.ManyToManyField(Categorie)
    description = models.TextField()
    requirment = models.TextField()
    loaction = models.CharField(max_length=200)
    vacancy = models.IntegerField(default=0)
    job_type = models.CharField(choices=CHOICES, blank=True, null=True)
    salary = models.IntegerField(default=0)
    applicants = models.ManyToManyField(
        User,
        related_name='applied_jobs',
        blank=True,
        limit_choices_to={'profile__role': 'Job Seeker'}
    )
    posted_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    
    
# 123456SI