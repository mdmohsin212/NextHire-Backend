from django.contrib import admin
from .models import *

# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('categorie',)}
    list_display = ['categorie', 'slug']
    
admin.site.register(Categorie, CategorieAdmin)

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']
    
admin.site.register(Company, CompanyAdmin)
admin.site.register(JobListing)