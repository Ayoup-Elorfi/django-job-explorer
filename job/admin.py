from django.contrib import admin
from .models import Job, Category, Candidate
# Register your models here.

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Candidate)
