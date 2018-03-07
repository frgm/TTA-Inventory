from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def adminInv(request):
    return render_to_response("adminInv.html")
    
def adminPro(request):
    return HttpResponse("adminPro")

def distribution(request):
    return HttpResponse("distribution")

def index(request):
    return HttpResponse("I N D E X")

def production(request):
    return HttpResponse("production")

def report(request):
    return HttpResponse("report")
