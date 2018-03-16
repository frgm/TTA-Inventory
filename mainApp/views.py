from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
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

class dbReport(View):
    @csrf_exempt
    def get(self, request):
        r = md.Products.objects.values_list('Name',flat=True)
        return HttpResponse(r)
        
    @csrf_exempt
    def post(self,request):
        for item in request:
            id = md.Products.objects.filter(Name=item).values('ID_Prod')
            r = md.Report(ID_Loc=request.session['ID_Loc_Usr'], ID_Emp=request.session['ID_Emp_Usr'], ID_Prod=id, Quantity=request[item], Date=dt.datetime.now().strftime("%d-%m-%Y"))
            r.save()
        return JsonResponse({'pk': r.pk});

class dbProduction(View):
    @csrf_exempt
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
        

class dbDistribution(View):
    @csrf_exempt
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


class dbAdminPro(View):
    @csrf_exempt
    def post(self, request):
        print(request.POST) 
        type = request.POST['type']
        data = request.POST['data']
        csvdata = csv.reader(data.split('\n'))
        if type == 'Employees':
            for row in csvdata:
                i = md.Employees(Name=row[0], Password=row[1], Role=row[2])
        elif type == 'Products':
            for row in csvdata:
                i = md.Products(Name=row[0], Material=row[1])
        elif type == 'Locations':
            for row in csvdata:
                i = md.Locations(Name=row[0], Address=row[1], Latitude=row[2], Longitude=row[3])
        else:
            return JsonResponse({'success': False})
        i.save()
        return JsonResponse({'success': True, 'pk': i.pk})

class dbAdminInv(View):
    @csrf_exempt
    def get(self, request):
        todayDate =  dt.datetime.now()
        today,precision = algo.predictRegression(todayDate.strftime("%d-%m-%Y"))
        tomorrow,_ = algo.predictRegression((todayDate + dt.timeDelta(days=1)).strftime("%d-%m-%Y"))
        pastValues = []
        for i in range(1,4):
            q = md.Requisition.objects.filter(ID_Loc=request.session['ID_Loc_Usr']).filter(Date = todayDate - dt.timeDelta(days= i))
            pastValues.append(q.Quantity)
        proyectedValues = []
        for i in range(2,5):
            p = algo.predictRegression((todayDate + dt.timeDelta(days=i)).strftime("%d-%m-%Y"))
            proyectedValues.append(p)
        return JsonResponse({'today': today, 'tomorrow': tomorrow, 'pastValues': pastValues, 'proyectedValues': proyectedValues, 'precision': precision})   
    
class login(View):
    @csrf_exempt
    def post(self, request):
        name = request.data.name
        pasw = request.data.pasw
        e = md.Employee.filter(Name=name).filter(Password=pasw)
        if not e.count():
            return JsonResponse({'success' : True, 'role' : e.Role})
        else:
            return JsonResponse({'success' : False})