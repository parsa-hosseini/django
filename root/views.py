from django.shortcuts import render
from .models import *

def index(request):
    services = sevices.objects.filter(status=True)
    spservices = sservices.objects.filter(status = True)
    ask = askes.objects.filter(status = True)
    tr = trainer.objects.filter(status = True)
    v1 = vijegit.objects.all()
    v2 = vijegif.objects.all()
    pr = price.objects.filter(status = True)
    return render(request , 'root/index.html' , context = {'services' : services , 
        'spservices' : spservices , 
        'ask' : ask , 
        'tr' : tr ,
        'v1' : v1 , 'v2' : v2 ,
        'pr' : pr , 
            })
