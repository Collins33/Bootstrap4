from django.shortcuts import render
from .models import Category,Ingredient,Confectionery

# Create your views here.
def welcome(request):
    categories=Category.objects.all()
    confectioneries=Confectionery.objects.all()
    return render(request,"index.html",{"categories":categories,"confectioneries":confectioneries})


def allSweets(request):
    sweets=Confectionery.objects.all()
    return render(request,"allSweets.html",{"sweets":sweets})    
