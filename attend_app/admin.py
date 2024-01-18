from django.contrib import admin

# Register your models here.
from .models import AttendanceEntry

admin.site.register(AttendanceEntry)