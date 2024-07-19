from django.shortcuts import render, redirect
from django.views import View
from .forms import EmployeeForm
from .models import Employee
from django.db.models import Q 
# Create your views here.

def employeeView(request):
        template_name = 'home/index.html'
        if request.method == 'GET':
            emp = Employee.objects.all()
            context = {'emp': emp}
            return render(request, template_name, context)
        if request.method == 'POST':
            emp = Employee.objects.all()
            context = {'emp': emp}
            return render(request, template_name, context)
        

def add_emp(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("emp")
    
    template_name = "home/add_emp.html"
    return render (request, template_name, locals())

    
def show_view(request):
    emp = Employee.objects.all()
    context = {'emp':emp}
    return render (request, 'home/delete.html', locals())


def delete_view(request, pk):
    # print(pk)
    sample = Employee.objects.get(pk=pk)
    if request.method == "POST":
        sample.delete()
        # print("---", pk)
        return redirect("emp")
    return render (request, 'home/delete.html', locals())

def filter_view(request):

    if request.method == "POST":
        print("Hi--new")
        name = request.POST.get('name')
        department = request.POST.get('dept')
        print(department)
        designation = request.POST.get('role')
        emps = Employee.objects.all()
        print("---", name)
        if name and department and  designation:
            emp = emps.filter((Q(first_name__icontains=name) | Q(last_name__icontains=name)), Department = department, Designation = designation)
            context = {'emp': emp}
        elif name and department:
            emp = emps.filter((Q(first_name__icontains=name) | Q(last_name__icontains=name)), Department = department)
            context = {'emp': emp}
        elif name:
            emp = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))  
            context = {'emp': emp}  
        elif designation:
            emp = emps.filter(Designation = designation)  
            context = {'emp': emp}
        elif department:
            print("hi")
            emp = emps.filter(Department = department) 
            print(emp)
            print("after this department") 
            context = {'emp': emp}

        return render(request, 'home/index.html', context)
    
    elif request.method == "GET":
        return render (request, 'home/filter.html', locals())