from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def adminInv(request):
    return render_to_response("adminInv.html")
    
def adminPro(request):
    return render_to_response("adminPro.html")

def distribution(request):
    return render_to_response("request.html")

def index(request):
    return render_to_response("index.html")

def production(request):
    return render_to_response("production.html")
    
def report(request):
    return render_to_response("report.html")