from django.shortcuts import render
from .models import Notice

# Create your views here.
def note(request):
    notices = Notice.objects
    return render(request, 'note.htm', {'notices':notices})