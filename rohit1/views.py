from django.http import HttpResponse
from django.shortcuts import render 
from AboutUs.models import AboutModel
from subscribe.models import Subscribe




def homePage(request):  
    Data=AboutModel.objects.all()

    data={
        'Data':Data
    }
    return render(request,"index.html",data)




def aboutus(request):
    aboutData=AboutModel.objects.all()

    data={
        'aboutData':aboutData
    }
    return render(request,"aboutus.html",data)
def service(request):  
    return render(request,"service.html")
def team(request):  
    return render(request,"team.html")
def why(request):  
    return render(request,"why.html")
def login(request):  
    return render(request,"login.html")
def subscribe(request):
    msg=''
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        alldata=Subscribe(fullname=fullname,email=email,phone=phone,message=message)
        alldata.save()
        msg="Data Inserted"
  
    return render(request,"subscribe.html",{'msg':msg})