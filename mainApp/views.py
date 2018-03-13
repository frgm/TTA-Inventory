from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views import View
import datetime as dt
import csv
import mainApp.models as md
import mainApp.algorithms as algo

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

class dbReport(view):
    def get(self, request):
        r = md.Products.objects.values_list('Name',flat=True)
        return HttpResponse(r)
    
    def post(self,request):
        for item in request:
            id = md.Products.objects.filter(Name=item).values('ID_Prod')
            r = md.Report(ID_Loc=request.session['ID_Loc_Usr'], ID_Emp=request.session['ID_Emp_Usr'], ID_Prod=id, Quantity=request[item], Date=dt.datetime.now().strftime("%d-%m-%Y"))
            r.save()
        return JsonResponse({'pk': r.pk});

class dbProduction(view):
    def get(self, request):
        prodVal = {}
        daysAgo = dt.datetime.now() - dt.timeDelta(days=2)
        repo = md.Reports.objects.filter(Date__lt = daysAgo)
        usage = {}
        for r in repo:
            usage[r.Date.strftime("%d-%m-%Y")] = r.Quantity
        dQuotas = md.Requisition.objects.filter(ID_Loc=request.session['ID_Loc_Usr']).filter(Date__lt = daysAgo)
        dUsage = algo.predictRegression(dt.datetime.now().strftime("%d-%m-%Y"))
        prodVal['usage'] = usage;
        prodVal['dailyQuotas'] = dQuotas;
        prodVal['dailyusage'] = dUsage;
        return HttpResponse(prodVal)
        

class dbDistribution(view):
    def get(self, request):
        locs = md.Locations.objects.All();
        locs_out = {};
        for loc in locs:
            itms = md.Stock.objects.filter(ID_Loc = loc.ID_Loc)
            i = {}
            for itm in itms:
                iname = md.Products.objects.filter(ID_Prod=itm.ID_Prod).get()
                i[iname] = itm.Quantity
            locs_out[loc.Name] = {"address" : loc.Address, "coords" : {lat : loc.Latitude, lng : loc.Longitude}, items : i}
        return HttpResponse(locs_out)


class dbAdminPro(view):
    def post(self, request):
        type = request.data.type
        data = request.data.data
        if type == 'CSVEMployee':
            csvdata = csv.reader(data)
            for row in csvdata:
                i = md.Employee(Login=csvdata[0], Pass=csvdata[1], Role=csvdata[2])
                i.save()
        elif type == 'CSVProducts':
            csvdata = csv.reader(data)
            for row in csvdata:
                i = md.Products(Name=csvdata[0], Material=csvdata[1])
                i.save()
        elif type == 'CSVLocations':
            csvdata = csv.reader(data)
            for row in csvdata:
                i = md.Locations(Name=csvdata[0], Address=csvdata[1], Latitude=csvdata[2], Longitude=csvdata[3])
                i.save()
        elif type == 'Employee':
                i = md.Employee(Login=data.Login, Pass=data.Pass, Role=data.Role)
                i.save()
        elif type == 'Products':
            i = md.Products(Name=data.Name, Material=data.Material)
            i.save()
        elif type == 'Locations':            
            i = md.Locations(Name=data.Name, Address=data.Address, Latitude=data.Latitude, Longitude=data.Longitude)
            i.save()
        return JsonResponse({'pk': i.pk})

class dbAdminInv(view): # {today: 20, tomorrow: 30, pastValues: [170,150,140], proyectedValues:[180,150,160], precision: 95};
    def get(self, request):
        todayDate =  dt.datetime.now()
        today = algo.predictRegression(todayDate.strftime("%d-%m-%Y"))
        tomorrow = algo.predictRegression((todayDate - dt.timeDelta(days=2)).strftime("%d-%m-%Y"))
        
    
class login(view):
    def post(self, request):
        name = request.data.name
        pasw = request.data.pasw
        e = md.Employee.filter(Name=name).filter(Password=pasw)
        if not e.count():
            return JsonResponse({'success' : True, 'role' : e.Role})
        else:
            return JsonResponse({'success' : False})