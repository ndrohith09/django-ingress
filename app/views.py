import os
from django.http import HttpResponse
# Create your views here.

def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print('ip address of the client = ' , ip)
    pod_name = os.environ.get('HOSTNAME') 


    return HttpResponse(
        '<h1>Hello World . ip address of the client = ' + str(ip) + '</h1>'
        '<h1>Hello World . pod name = ' + str(pod_name) + '</h1>' 
        )

def page(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print('ip address of the client = ' , ip)
    pod_name = os.environ.get('HOSTNAME') 


    return HttpResponse(
        '<h1>Hello World . ip address of the client = ' + str(ip) + '</h1>'
        '<h1>Hello World . pod name = ' + str(pod_name) + '</h1>' 
        )
