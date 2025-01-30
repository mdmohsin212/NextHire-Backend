from django.db import models
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
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
    description = models.TextField()
    requirment = models.TextField()
    loaction = models.CharField(max_length=200)
    vacancy = models.IntegerField(default=0)
    job_type = models.CharField(choices=CHOICES, blank=True, null=True)
    salary = models.IntegerField(default=0)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

CHOICES_STATUS = [
    ("Approved", "Approved"),
    ("Pending", "Pending"),
    ("Rejected", "Rejected")
]
    
class AppliedJob(models.Model):
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applied_jobs_as_candidate', limit_choices_to={'profile__role': 'Job Seeker'})
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applied_jobs_as_employer',
    limit_choices_to={'profile__role': 'Employer'})
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default="Pending")
    applicant_name = models.CharField(max_length=100)
    task = models.TextField(null=True, blank=True)
    final_dateline = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    submit_status = models.CharField(max_length=20, choices=CHOICES_STATUS, default="Pending")
    is_jobAssign = models.BooleanField(default=False)
    Submit_Job = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"
    
    def save(self, *args, **kwargs):
        email_subject = ""
        email_body = ""
        if self.status == "Approved":
            email_subject = f"Congratulations! Your application for {self.job.title} is approved"
            email_body = f"""
            Hi {self.candidate.first_name} {self.candidate.last_name},
            Congratulations! Your application for the position "{self.job.title}" at "{self.job.company.name}" has been approved.
            Best regards,
            {self.employer.first_name} {self.employer.last_name}
            """

        elif self.status == "Rejected":
            email_subject = f"Your application for {self.job.title} has been rejected"
            email_body = f"""
            Hi {self.candidate.first_name} {self.candidate.last_name},
            We regret to inform you that your application for the position "{self.job.title}" at "{self.job.company.name}" has been rejected.
            Thank you for your interest, and we wish you the best in your job search.
            Best regards,
            {self.employer.first_name} {self.employer.last_name}
            """
            
        if len(email_subject) != 0 and len(email_body) != 0:
            email = EmailMultiAlternatives(
            subject=email_subject,
            body=email_body,
            to=[self.candidate.email]
            )
            email.send()
            
        super().save(*args, **kwargs)

# 123456SI