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

# def updateDepartment(request, did):
#     if request.method == "GET":
#         d = Department.objects.filter(dept_id=did) 
#         context = {}
#         context['department'] = d #in case if we use get
#         return render(request,'updatedepartment.html',context)
#     else:
#         dep = Department.objects.filter(dept_id = did)
#         # d is the queryset, on Queryset, we can call update and delete
#         n = request.POST['dept_name']
#         d = request.POST['description']
#         dep.update(dept_name=n, description =d)
#         return redirect('/')

def update_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    
    if request.method == 'POST':
        department.dept_name = request.POST.get('dept_name')
        department.description = request.POST.get('description')
        department.save()
        
    return render(request, 'update_department.html', {'department': department})




