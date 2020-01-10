from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from MyUser.models import MyUser
from patient.models import Patient




def patients(request):
    if request.user.is_authenticated:
        return render(request,'patients.html')
    else:
        return redirect('login')

def dashboard(request):
    return render(request,'dashboard.html')        


def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('patients')
        else:
            return redirect('login')
    else:
        return render(request,'login.html',{})

def register(request):
    if request.method=='POST':
        d =True
        e = request.POST.get('email')
        c = request.POST.get('contact')
        p1 = request.POST.get('password')
        p2= request.POST.get('pass')
        u =MyUser(email=e,contact_no=c,is_doctor=d)
        if p1==p2:
            u.set_password(p1)
        else:
            pass
        u.save()
        return render(request,"register.html")
    else:
        return render(request,"register.html")

def patients(request):
    if request.method=='POST':
        #d = request.POST.get('date')
        n = request.POST.get('name')
        ag = request.POST.get('age')
        a = request.POST.get('address')
        c= request.POST.get('contact_no')


        u =Patient(name= n,age=ag,address=a,contact_no=c)
        u.save()
        return render(request,"patients.html")
    else:
        return render(request,"patients.html")
