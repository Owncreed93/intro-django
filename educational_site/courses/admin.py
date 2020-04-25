from django.contrib import admin

# Register your models here.
from .models import Course

# * REGISTER THE COURSE AS A MODULE
admin.site.register(Course)