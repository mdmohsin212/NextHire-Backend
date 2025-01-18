from django.db import models
from job.models import JobListing, AppliedJob
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your models here.

class JobApplication(models.Model):
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'profile__role' : 'Job Seeker'}, related_name='applications')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website_url = models.CharField(max_length=200,blank=True, null=True)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    cv = models.FileField(upload_to='applications/')
    letter = models.TextField(blank=True)
    applied_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.job_seeker.first_name} {self.job_seeker.last_name} - {self.job.title}"
    
    def save(self,*args, **kwargs):    
        super(JobApplication, self).save(*args, **kwargs)
        
        applied_job = AppliedJob.objects.create(
            candidate=self.job_seeker,
            job=self.job,
            employer=self.job.employer,
            applicant_name=self.job_seeker.username,
            status="Pending",
            )
        applied_job.save()
        
        email_subject = f"New Job Application for {self.job.title}"
        email_body = render_to_string('new_applicant.html', {'job' : self.job, 'applicant' : self})
            
        email = EmailMultiAlternatives(email_subject, '', to=[self.job.employer.email])
        email.attach_alternative(email_body, "text/html")
        email.send()