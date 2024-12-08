from django.shortcuts import render,redirect
from DepartmentApp.models import Department
from django.http import HttpResponse, Http404

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
#         context['department'] = d
#         return render(request,'updatedepartment.html',context)
#     else:
#         dep = Department.objects.filter(dept_id = did)
#         n = request.POST['dept_name']
#         d = request.POST['description']
#         dep.update(dept_name=n, description =d)
#         return redirect('/')

def updateDepartment(request, did):
    try:
        # Fetch the department by ID or raise a 404 error if not found
        department = Department.objects.get(dept_id=did)
    except Department.DoesNotExist:
        return HttpResponse("Department not found", status=404)

    if request.method == "GET":
        # Render the form with the existing department details
        return render(request, 'updatedepartment.html', {'department': department})

    elif request.method == "POST":
        # Get updated values from the POST request
        department.dept_name = request.POST.get('dept_name', department.dept_name)
        department.description = request.POST.get('description', department.description)
        # Save the changes to the database
        department.save()
        # Redirect to the home page after updating
        return redirect('/')



