from django.contrib import admin
from .models import *

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']
    
admin.site.register(Company, CompanyAdmin)
admin.site.register(JobListing)