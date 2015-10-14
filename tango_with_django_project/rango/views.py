from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = { 'boldmessage': "I am Bold From Context"}
    return render(request, 'rango/index.html', context_dict)
#    return HttpResponse("Hello World from first page!")
