from covid.models import covid_db
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html', {'name': 'Addition using Forms'})

def send(request):
    if request.method == 'POST':
        aadhar = request.POST['ID']
        name = request.POST['data1']
        age = request.POST['data2']
        address = request.POST['data3']
        # covid_db(ID = ID,data1=data1,data2=data2,data3=data3).save()
        covid_db(name=name, age=age, aadhar=aadhar, address=address).save()
        msg="Data Stored Successfully"
        return render(request,"index.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")