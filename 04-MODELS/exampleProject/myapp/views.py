from django.shortcuts import render
from myapp.models import *

# Create your views here.
def index(request):
    data = Ogrenci.objects.all()
    ogrenciler = {
        "ogrenciler":data
    }
    return render(request,'index.html',ogrenciler)