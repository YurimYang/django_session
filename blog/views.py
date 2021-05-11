from django.shortcuts import render
from .models import Blog

# Create your views here.
def hello(request):
    return render(request, "hello.htm")

def home(request):
    blogs = Blog.objects
    return render(request, 'home.htm', {'blogs':blogs})