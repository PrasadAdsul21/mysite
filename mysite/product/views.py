from django.shortcuts import render
from django.http import HttpResponse
from product.models import  Product


def about(request):
    return HttpResponse("HELLO")
def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})