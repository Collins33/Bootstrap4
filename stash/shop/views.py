from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from django.http import HttpResponse,Http404,HttpResponseRedirect

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


def candy(request,candy_id):
    try:
        candy=Confectionery.objects.get(id=candy_id)
    except DoesNotExist:
        raise Http404()

    return render(request,"candy.html",{"candy":candy})        

