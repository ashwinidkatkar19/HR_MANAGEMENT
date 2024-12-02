from django.shortcuts import render,redirect
from DepartmentApp.models import Department

# Create your views here.
def home(request):
    data=Department.objects.filter(status=True)
    context={}
    context['department']= data
    return render(request,'index.html',context)

def createDepartment(request):
    if request.method == 'GET':
        return render(request,'createdepartment.html')
    else:
        n = request.POST['dept_name']
        d = request.POST['description']
        dept = Department.objects.create(dept_name=n, description =d)
        dept.save()
        return redirect('/')
    
def Deletedepartment(request, dept_id):
    dept = Department.objects.get(dept_id = dept_id)
    dept.status=False
    print(dept)
    print(dept.status)
    dept.save()
    return redirect('/')

def updateDepartment(request, did):
    if request.method == "GET":
        d = Department.objects.filter(dept_id=did) 
        context = {}
        context['department'] = d #in case if we use get
        return render(request,'updatedepartment.html',context)
    else:
        dep = Department.objects.filter(dept_id = did)
        # d is the queryset, on Queryset, we can call update and delete
        n = request.POST['dept_name']
        d = request.POST['description']
        dep.update(dept_name=n, description =d)
        return redirect('/')
    

# def home(request):
#     data = Department.objects.all()
#     context = {'department': data}
#     return render(request, 'index.html', context)

# View for creating a department
# def createDepartment(request):
#     if request.method == 'GET':
#         return render(request, 'createdepartment.html')
#     else:
#         n = request.POST['dept_name']
#         d = request.POST['description']
#         dept = Department.objects.create(dept_name=n, description=d)
#         dept.save()
#         return redirect('/')

# def showHome(request):
#     # Only get active departments
#     data = Department.objects.filter(status=True)
#     context = {'departs': data}
#     return render(request, 'index.html', context)


# def addDepart(request):
#     print(request.method)
#     if request.method=='GET':
#         return render(request,'adddepart.html')
#     else:
#         #capture data from form
#         n = request.POST['depart_name']
#         d = request.POST['description']
#         print(n,d)

        #add the data in db
        # d=Department.objects.create(depart_name=n,description=d)
        # d.save()
        # # return render(request,'index.html')
        # # return render(request,'index.html',context)
        # return redirect('/')


# def Updatedepart(request,departid):
#     # b=Depart.objects.filter(id=bookid)
#     d=Department.objects.get(dept_id=departid) 
#     if request.method=='GET':
#         context={}
#         context['depart']=d # used with GET method
#         return render(request,'updatedepart.html',context)
#     else:
#         dt=Department.objects.filter(dept_id=departid)
#         n=request.POST['depart_name']
#         d=request.POST['description']
#         dt.update(depart_name=n,description=d)
#         return redirect('/')
    
# def Deletedepart(request, departid):
#     # Get the department object
#     depart = Department.objects.get(dept_id=departid)
#     # Update the status to False (inactive)
#     depart.status = False
#     depart.save()  # Save the updated status to the database
#     return redirect('/')

