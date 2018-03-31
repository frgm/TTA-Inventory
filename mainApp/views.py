from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import datetime as dt
import csv
import mainApp.models as md
import mainApp.algorithms as algo
import json

def adminInv(request):
    if 'Role' not in request.session or request.session['Role'] != 'admin' :
        return render_to_response("error.html")
    return render_to_response("adminInv.html")
    
def adminPro(request):
    #if 'Role' not in request.session or request.session['Role'] != 'pro':
    #    return render_to_response("error.html")
    return render_to_response("adminPro.html")

def distribution(request):
    if 'Role' not in request.session or request.session['Role'] != 'distribution':
        return render_to_response("error.html")
    return render_to_response("distribution.html")

def index(request):
    return render_to_response("index.html")

def production(request):
    if 'Role' not in request.session or request.session['Role'] != 'production':
        return render_to_response("error.html")
    return render_to_response("production.html")
    
def report(request):
    if 'Role' not in request.session or request.session['Role'] != 'report':
        return render_to_response("error.html")
    return render_to_response("report.html")

class dbReport(View):
    @csrf_exempt
    def get(self, request):
        r = md.Products.objects.values_list('Name',flat=True)
        items = ""
        for item in r:
            items = "%s,%s" % (items, item)
        return JsonResponse({'success': True, 'items': items[1:]})
        
    @csrf_exempt
    def post(self,request):
        try:
            report = json.loads(request.POST['report'])
            print(report)
            for item in report:
                prod = md.Products.objects.get(Name=item)
                loc = md.Locations.objects.get(ID_Loc=request.session['ID_Loc_Usr'])
                emp = md.Employees.objects.get(ID_Emp=request.session['ID_Emp_Usr'])
                r = md.Report(ID_Loc=loc, ID_Emp=emp, ID_Prod=prod, Quantity=report[item], Date=dt.datetime.now())
                r.save()
            return JsonResponse({'success': True, 'pk': r.pk})
        except Exception as ex:
            return JsonResponse({'success': False, 'exception':type(ex).__name__,})

class dbProduction(View):
    @csrf_exempt
    def get(self, request):
        prodVal = {}
        daysAgo = dt.datetime.now() - dt.timedelta(days=2)
        try:
            #req = md.Requisition.objects.filter(Date__lt = daysAgo)
            req = md.Requisition.objects.filter(Date = dt.datetime.now())
            usage = {}
            for r in req:
                usage[r.Date.strftime("%d-%m-%Y")] = r.Quantity
        except:
            usage = {"error":-1}         
        try:
            #rep = md.Report.objects.filter(Date__lt = daysAgo)
            rep = md.Report.objects.filter(Date = dt.datetime.now())
            dQuotas = {}
            for r in rep:
                prod = md.Products.objects.get(ID_Prod= r.ID_Prod)
                usage[prod.Name] = r.Quantity
        except:
            dQuotas = {"error":-1}            
        dUsage,_ = algo.predictRegression(dt.datetime.now().strftime("%d-%m-%Y"))
        prodVal['usage'] = json.dumps(usage)
        prodVal['dailyQuotas'] = json.dumps(dQuotas)
        prodVal['dailyusage'] = dUsage
        prodVal['success'] = True
        loc = md.Locations.objects.get(ID_Loc=request.session['ID_Loc_Usr'])
        r = md.PredictedRequisition(ID_Loc=loc, Quantity=dUsage, Date=dt.datetime.now())
        r.save()
        print(prodVal)
        return JsonResponse(prodVal)

    def post(self, request):
        todayDate =  dt.datetime.now()
        qnt = request.POST['quantity']
        loc = md.Locations.objects.get(ID_Loc=request.session['ID_Loc_Usr'])
        r = md.Requisition(ID_Loc=loc, Quantity=qnt, Date=dt.datetime.now())
        r.save()        

class dbDistribution(View):
    @csrf_exempt
    def get(self, request):
        locs = md.Locations.objects.all()
        locs_out = {};
        for loc in locs:
            itms = md.Restock.objects.filter(ID_Loc = loc.ID_Loc)
            i = {}
            for itm in itms:
                iname = md.Products.objects.filter(ID_Prod=itm.ID_Prod).get()
                i[iname] = itm.Quantity
            locs_out[loc.Name] = {"address" : loc.Address, "coords" : {'lat' : loc.Latitude, 'lng' : loc.Longitude}, 'items' : i}
        locs_out['success'] = True
        return JsonResponse(locs_out)

class dbAdminPro(View):
    @csrf_exempt
    def post(self, request):
        #print(request.POST) 
        type = request.POST['type']
        data = request.POST['data']
        csvdata = csv.reader(data.split('\n'))
        if type == 'Employees':
            for row in csvdata:
                i = md.Employees(Name=row[0], Password=row[1], Role=row[2], ID_Loc=row[3])
        elif type == 'Products':
            for row in csvdata:
                i = md.Products(Name=row[0], Material=row[1])
        elif type == 'Locations':
            for row in csvdata:
                i = md.Locations(Name=row[0], Address=row[1], Latitude=row[2], Longitude=row[3])
        elif type == 'Restock':
            for row in csvdata:
                loc = md.Locations.objects.get(ID_Loc=row[0])
                prod = md.Products.objects.get(ID_Prod=row[1])
                i = md.Restock(ID_Loc=loc, ID_Prod=prod, Quantity=row[2])
        else:
            return JsonResponse({'success': False})
        i.save()
        return JsonResponse({'success': True, 'pk': i.pk})

class dbAdminInv(View):
    @csrf_exempt
    def get(self, request):
        todayDate =  dt.datetime.now()
        today,precision = algo.predictRegression(todayDate.strftime("%d-%m-%Y"))
        tomorrow,_ = algo.predictRegression((todayDate + dt.timedelta(days=1)).strftime("%d-%m-%Y"))
        pastValues = []
        for i in range(1,4):
            q = md.Requisition.objects.filter(ID_Loc=request.session['ID_Loc_Usr']).filter(Date = todayDate - dt.timedelta(days= i))
            pastValues.append(q[0].Quantity)
        proyectedValues = []
        for i in range(2,5):
            p,_ = algo.predictRegression((todayDate + dt.timedelta(days=i)).strftime("%d-%m-%Y"))
            proyectedValues.append(p)
        return JsonResponse({success: True, 'today': today, 'tomorrow': tomorrow, 'pastValues': pastValues, 'proyectedValues': proyectedValues, 'precision': precision})   
        
class login(View):
    @csrf_exempt
    def post(self, request):
        name = request.POST['name']
        pasw = request.POST['pasw']
        e = md.Employees.objects.filter(Name=name).filter(Password=pasw)
        if e.count():
            print(e.query)
            request.session['ID_Loc_Usr'] = e[0].ID_Loc
            request.session['ID_Emp_Usr'] = e[0].ID_Emp
            request.session['Role'] = e[0].Role
            return JsonResponse({'success' : True, 'role' : e[0].Role})
        else:
            return JsonResponse({'success' : False})