from django.shortcuts import render,HttpResponse
from . models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone=int(request.POST['phone'])
        salary=int(request.POST['salary'])
        dept=int(request.POST['dept'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        new_emp=Employee(first_name=first_name,last_name=last_name,phone=phone,salary=salary,dept_id=dept,bonus=bonus,role_id=role,hire_data=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added ")
    elif request.method=="GET":
        return render(request,'add_emp.html')
    else:
        return HttpResponse("Exception occured ")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_remove=Employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse("Deleted Successfully")
        except:
            return HttpResponse("Enter a valid ID")

    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context) 
    
def filter_emp(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=dept)
        context={
            'emps':emps
        }
       
        return render(request,'all_emp.html',context)

    elif request.method=='GET':
        return render (request,'filter_emp.html')
    
    else:
        return HttpResponse('An exception occured')

# return render(request,'filter_emp.html')