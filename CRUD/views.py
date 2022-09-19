from django.shortcuts import render
from .models import Employee
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class EmployeeCreate(CreateView):
    model=Employee
    template_name="employee_form.html"
    fields="__all__"
    success_url='/list'

class Employeelist(ListView):
    model=Employee
    template_name="employee_list.html"
    def get_queryset(self):
        qs=Employee.objects.all()
        return qs

class Employeedetail(DetailView):
    model=Employee
    template_name="employee_detail.html"

class Employeeupdate(UpdateView):
    model=Employee
    template_name="employee_form.html"
    fields='__all__'
    success_url='/list'

class Employeedelete(DeleteView):
    model=Employee
    template_name='template_confirm_delete.html'
    success_url='/list'