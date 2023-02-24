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
    pod_ip = os.environ.get('POD_IP')


    return HttpResponse(
        '<h1>Hello World . ip address of the client = ' + ip + '</h1>'
        '<h1>Hello World . pod name = ' + pod_name + '</h1>'
        '<h1>Hello World . pod ip = ' + pod_ip + '</h1>'
        )

def page(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print('ip address of the client = ' , ip)
    pod_name = os.environ.get('HOSTNAME')
    pod_ip = os.environ.get('POD_IP')


    return HttpResponse(
        '<h1>Page 2 . ip address of the client = ' + ip + '</h1>'
        '<h1>Page 2 . pod name = ' + pod_name + '</h1>'
        '<h1>Page 2 . pod ip = ' + pod_ip + '</h1>'
        )
