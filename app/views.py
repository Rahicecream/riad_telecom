from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Bank,Cement,Telecom,Personal

from django.contrib import messages

from django.db.models import Sum
# Create your views here.
set_value=0

@login_required(login_url='login')
def home(request):
    bank_get=Bank.objects.all().aggregate(Sum('get_amount'))
    bank_give=Bank.objects.all().aggregate(Sum('give_amount'))

    telecom_get=Telecom.objects.all().aggregate(Sum('get_amount'))
    telecom_give=Telecom.objects.all().aggregate(Sum('give_amount'))

    cement_get=Cement.objects.all().aggregate(Sum('get_amount'))
    cement_give=Cement.objects.all().aggregate(Sum('give_amount'))


    personal_get=Personal.objects.all().aggregate(Sum('get_amount'))
    personal_give=Personal.objects.all().aggregate(Sum('give_amount'))


    context={
        'total_bank_get':bank_get['get_amount__sum'],
        'total_bank_give':bank_give['give_amount__sum'],
        'bank_cash':(bank_get['get_amount__sum']-bank_give['give_amount__sum']),

        'total_telecom_get':telecom_get['get_amount__sum'],
        'total_telecom_give':telecom_give['give_amount__sum'],
        'telecom_cash':(telecom_get['get_amount__sum']-telecom_give['give_amount__sum']),

        'total_cement_get':cement_get['get_amount__sum'],
        'total_cement_give':cement_give['give_amount__sum'],
        'cement_cash':(cement_get['get_amount__sum']-cement_give['give_amount__sum']),

        'total_personal_get':personal_get['get_amount__sum'],
        'total_personal_give':personal_give['give_amount__sum'],
        'personal_cash':(personal_get['get_amount__sum']-personal_give['give_amount__sum']),
    }



    return render(request,'home.html',context)

#bank_trasaction
@login_required(login_url='login')
def bank_get(request):
    if request.method=='POST':
        get_data=Bank(name=request.POST.get('bank_get_name'),get_amount=request.POST.get('bank_get_amount'),give_amount=set_value)

        get_data.save()
        messages.success(request, 'Your record add successfully')


    return render(request,'bank_get.html',{'title':'Bank'})

@login_required(login_url='login')
def bank_give(request):
    if request.method=='POST':
        get_data=Bank(name=request.POST.get('bank_give_name'),get_amount=set_value,give_amount=request.POST.get('bank_give_amount'))

        get_data.save()
        messages.success(request, 'Your record add successfully')
    return render(request,'bank_give.html')


#cement_transaction
@login_required(login_url='login')
def cement_get(request):
    if request.method=='POST':
        get_data=Cement(name=request.POST.get('cement_get_name'),get_amount=request.POST.get('cement_get_amount'),give_amount=set_value)

        get_data.save()
        messages.success(request, 'Your record add successfully')

    return render(request,'cement_get.html',{'title':'Cement'})


@login_required(login_url='login')
def cement_give(request):
    if request.method=='POST':
        get_data=Cement(name=request.POST.get('cement_give_name'),get_amount=set_value,give_amount=request.POST.get('cement_give_amount'))

        get_data.save()
        messages.success(request, 'Your record add successfully')
    return render(request,'cement_give.html',{'title':'Cement'})


@login_required(login_url='login')
def telecom_get(request):
    if request.method=='POST':
        get_data=Telecom(name=request.POST.get('telecom_get_name'),get_amount=request.POST.get('telecom_get_amount'),give_amount=set_value)

        get_data.save()
        messages.success(request, 'Your record add successfully')
    return render(request,'telecom_get.html',{'title':'Telecom'})


@login_required(login_url='login')
def telecom_give(request):
    if request.method=='POST':
        get_data=Telecom(name=request.POST.get('telecom_give_name'),get_amount=set_value,give_amount=request.POST.get('telecom_give_amount'))

        get_data.save()
        messages.success(request, 'Your record add successfully')
    return render(request,'telecom_give.html',{'title':'Telecom'})


@login_required(login_url='login')
def personal_get(request):
    if request.method=='POST':
        get_data=Personal(name=request.POST.get('personal_get_name'),get_amount=request.POST.get('personal_get_amount'),give_amount=set_value)

        get_data.save()
        messages.success(request, 'Your record add successfully')
    return render(request,'personal_get.html',{'title':'Personal'})

@login_required(login_url='login')
def personal_give(request):
    if request.method=="POST":
        get_data=Personal(name=request.POST.get('personal_give_name'),get_amount=set_value,give_amount=request.POST.get('personal_give_amount'))

        get_data.save()
        messages.success(request, 'Your record add successfully')
    return render(request,'personal_give.html',{'title':'Personal'})



def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request, 'You have Logged in successfully')
            return redirect('home')
        else:
            messages.success(request, 'Please Enter Correct Username and Password to Login')
            return redirect('login')

    return render(request,'login.html')

def user_logout(request):
    logout(request)

    return redirect('login')

def rahi(request):
    return render(request,"rahi.html")
