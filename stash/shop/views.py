from django.shortcuts import render
from .models import Category

# Create your views here.
def welcome(request):
    categories=Category.objects.all()
    
    return render(request,"index.html",{"categories":categories})
