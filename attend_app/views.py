# attendance_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import AttendanceEntry

def home(request):
    return render(request, 'home.html')

@login_required
def start_attendance(request):
    if request.method == 'POST':
        entry = AttendanceEntry(user=request.user, entry_time=timezone.now())
        entry.save()
    return redirect('home')

@login_required
def end_attendance(request):
    if request.method == 'POST':
        entry = AttendanceEntry.objects.filter(user=request.user, exit_time__isnull=True).latest('entry_time')
        entry.exit_time = timezone.now()
        entry.save()
    return redirect('home')  

@login_required
def calculate_working_hours(request):
    entries = AttendanceEntry.objects.filter(user=request.user)
    total_working_seconds = sum((entry.exit_time - entry.entry_time).total_seconds() for entry in entries if entry.exit_time)
    total_break_seconds = sum((next_entry.entry_time - entry.exit_time).total_seconds() for entry, next_entry in zip(entries, entries[1:]) if entry.exit_time and next_entry.entry_time)
    
    # Convert total seconds to hours and remaining minutes
    total_working_hours, remainder = divmod(total_working_seconds, 3600)
    total_working_minutes = remainder // 60

    total_break_hours, remainder = divmod(total_break_seconds, 3600)
    total_break_minutes = remainder // 60

    return render(request, 'total_hours.html', {
        'total_working_hours': total_working_hours,
        'total_working_minutes': total_working_minutes,
        'total_break_hours': total_break_hours,
        'total_break_minutes': total_break_minutes,
    })

