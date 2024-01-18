# attendance_app/models.py
from django.db import models
from django.contrib.auth.models import User

class AttendanceEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"  {self.user}  {self.exit_time}"